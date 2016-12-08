# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from gm.models import GM
from gm.models import Server
from django.db.models import signals
from scheduler import scheduler
from django.utils import timezone
from multiprocessing.dummy import Pool
from gm.models import Send2GMServer
from django.utils.translation import ugettext as LOC


class GameMailRecordGroup(models.Model):
    gm = models.ForeignKey(GM, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    is_to_whole_accounts = models.BooleanField()
    create_date = models.DateTimeField()
    send_date = models.DateTimeField()
    sended = models.BooleanField(default=False)

    def get_mails(self):
        return self.gamemailrecord_set.all()

    def get_accs(self):
        return self.gamemailaccrecord_set.all()

    def get_target_accounts(self):
        return self.gamemailtargetaccountrecord_set.all()

    def get_state(self):
        mails = self.get_mails()
        if not self.sended:
            return ""
        ret_state = "success"
        for mail in mails:
            state = mail.get_state()
            if state == "fail":
                return "fail"
            if state == "error":
                return "error"
            if state == "sending":
                ret_state = "sending"
        return ret_state

    def get_state_html(self):
        state = self.get_state()
        if state == 'fail':
            return "<span class='fui-alert-circle'></span>"
        elif state == "error":
            return "<span class='fui-alert-circle'></span>"
        elif state == "success":
            return "<span class='fui-check'></span>"
        elif state == "sending":
            return "<span class='fui-upload'></span>"
        return ""


class GameMailRecord(models.Model):
    server = models.ForeignKey(Server, on_delete=models.SET_NULL, null=True)
    result = models.CharField(max_length=500, null=True, blank=True)
    group = models.ForeignKey(GameMailRecordGroup, on_delete=models.CASCADE)
    last_send_date = models.DateTimeField(null=True)
    send_lock = models.NullBooleanField()

    def get_state(self):
        group = self.group
        if not group.sended:
            return ""

        if self.result is None:
            if self.last_send_date is None:
                return "sending"

            now = timezone.now()
            past = (now - self.last_send_date).total_seconds()
            # 如果超过2分钟没有回包，视为失败
            if past >= 2 * 60:
                return "fail"
            return "sending"
        if self.result == "1":
            return "success"
        elif self.result == "404":
            return "fail"
        else:
            return "error"

    def get_state_html(self):
        state = self.get_state()
        if state == 'fail':
            return "<span class='text-warning'>" + LOC(u'out_of_time') + "</span>"
        elif state == "error":
            return "<span class='text-danger'>" + LOC(u'error_code') + ":" + self.result + "</span>"
        elif state == "success":
            return "<span class='text-success'>" + LOC(u'success') + "</span>"
        elif state == "sending":
            return "<span class='text-info'>" + LOC(u'sending') + "</span>"

        return ""

    def get_state_icon_html(self):
        state = self.get_state()
        if state == 'fail' or state == "error":
            return "<a herf='#' data-tag='re_link' data-re='" + str(
                self.id) + "' class='glyphicon glyphicon-repeat' onmouseover='' style='cursor: pointer;' data-toggle='tooltip' data-placement='left' title='" + LOC(u'resend_mail_tip') + "'>" + LOC(u'resend') + "</a>"

        return ""


class GameMailTargetAccountRecord(models.Model):
    account = models.CharField(max_length=100)
    group = models.ForeignKey(GameMailRecordGroup, on_delete=models.CASCADE)


class GameMailAccRecord(models.Model):
    item_id = models.CharField(max_length=30, null=True)
    item_type = models.CharField(max_length=30, null=True)
    num = models.IntegerField()
    group = models.ForeignKey(GameMailRecordGroup, on_delete=models.CASCADE)

    type_map = {u'coin': LOC(u'coin'), u'item': LOC(u'item'), u'diamond': LOC(u'diamond')}

    def get_type(self):
        return self.type_map.get(self.item_type, '')

    def get_id(self):
        if self.item_id:
            return self.item_id
        return ''


def send_out(mail):
    group = mail.group
    addressee_list = []
    if not group.is_to_whole_accounts:
        target_accounts = group.get_target_accounts()
        for target in target_accounts:
            addressee_list.append({u"actor_rid": int(target.account)})

    acc_list = []
    accs = group.get_accs()
    for acc in accs:
        id = None
        if acc.item_id is not None:
            id = int(acc.item_id)
        elif acc.item_type is not None:
            id = acc.item_type
        else:
            raise Exception("acc's id and type is both nil")
        acc_list.append({u"id": id, u"count": int(acc.num)})

    obj = {u'msg_id': u'mail', u'mail_id': mail.id, u"addressee_list": addressee_list, u"title": group.title,
           u"content": group.content,
           u"acc_list": acc_list}
    ret = Send2GMServer(obj, mail.server.id)
    return (mail, ret)


def send_mail_done_callback(tul):
    mail = tul[0]
    ret = tul[1]
    mail.result = ret
    mail.send_lock = False
    mail.save()


class GameMailWorker():
    def __init__(self, gamemail_group):
        pool = Pool(processes=4)
        mails = gamemail_group.get_mails()
        for mail in mails:
            mail.send_lock = True
            mail.last_send_date = timezone.now()
            mail.save()
            pool.apply_async(send_out, args=(mail,), callback=send_mail_done_callback)
        pool.close()


# 定时逻辑
def call_execute_mails(mailgroup):
    mailgroup.sended = True
    mailgroup.save()
    GameMailWorker(mailgroup)


def resend_mail(mail):
    if not mail.send_lock:
        mail.result = None
        mail.last_send_date = timezone.now()
        mail.send_lock = True
        mail.save()
        pool = Pool(processes=1)
        pool.apply_async(send_out, args=(mail,), callback=send_mail_done_callback)
        pool.close()


news_in_scheduler = {}


def on_mailgroup_create(mailgroup):
    now = timezone.now()
    send_date = mailgroup.send_date
    if now > send_date:
        # 如果在一分钟之内 视为立刻发送
        past = (now - send_date).total_seconds()
        is_immediately = (past <= 120)
        if is_immediately:
            print("[gamemail]execute immediately")
            call_execute_mails(mailgroup)
        else:
            print("[gamemail]notify_news_change: " + str(mailgroup.send_date) + " out of date,drop it")
        return

    job = news_in_scheduler.get(mailgroup.id)
    if not job:
        insert_2_scheduler(mailgroup)
        print('insert_news_of_notice')
    else:
        print('error : mailgroup already insert ')


def insert_2_scheduler(mailgroup):
    job = scheduler.add_job(call_execute_mails, 'date', run_date=mailgroup.send_date, args=[mailgroup])
    news_in_scheduler[mailgroup.id] = job


def init_scheduler_from_database():
    records = GameMailRecordGroup.objects.all()
    now = timezone.now()
    for rec in records:
        if not rec.sended:
            send_date = rec.send_date
            if now > send_date:
                print("[gamemail] " + str(send_date) + " out of date,drop it")
            else:
                insert_2_scheduler(rec)


# 可能在发送邮件时关闭了网站，启动网站时清掉锁
def clear_mail_lock():
    mails = GameMailRecord.objects.all()
    for mail in mails:
        mail.send_lock = False
        mail.save()


def notify_news_delete(sender, instance, **kwargs):
    job = news_in_scheduler.get(instance.id)
    if not job:
        print("error:job not created but delete?")
        return
    job.remove()
