# coding=utf-8
from django.db.models import signals
from scheduler import scheduler
from django.utils import timezone
from multiprocessing.dummy import Pool
from gm.models import Send2GMServer
from models import FlashNewsRecord

def send_out(message, server):
    obj = {u'msg_id': u'world_msg', u'content': message}
    ret = Send2GMServer(obj, server.id)
    return (server.id, ret)


class SendFlashNewsRecordWorker():
    def __init__(self, news):
        self.news = news
        servers = news.servers.all()
        self.servers = servers
        self.rets = []

        pool = Pool(processes=4)

        def callback(tul):
            self.rets.append(tul)
            if len(self.rets) == len(self.servers):
                self.news.result = str(self.rets)
                self.news.save()
                print("[SendFlashNewsRecordWorker]Done")

        for server in servers:
            pool.apply_async(send_out, args=(news.content, server), callback=callback)
        pool.close()


# 定时逻辑
def call_execute_news(news):
    news.sended = True
    news.save()
    SendFlashNewsRecordWorker(news)


news_in_scheduler = {}


def insert_news_of_notice(news):
    job = scheduler.add_job(call_execute_news, 'date', run_date=news.send_date, args=[news])
    news_in_scheduler[news.id] = job


def init_scheduler_from_database():
    records = FlashNewsRecord.objects.all()
    now = timezone.now()
    for rec in records:
        if not rec.sended:
            send_date = rec.send_date
            if now > send_date:
                print("[flashnews] " + str(send_date) + " out of date,drop it")
            else:
                insert_news_of_notice(rec)
    scheduler.print_jobs()





# 监听写入或者删除noticerecord数据
def notify_news_change(sender, instance, created, **kwargs):
    if instance.sended:
        return
    # 保存多键值对象时，需要save两次，这里用servers判断是否创建完毕
    if not instance.servers.all():
        return
    now = timezone.now()
    send_date = instance.send_date
    if now > send_date:
        # 如果在一分钟之内 视为立刻发送
        past = (now - send_date).total_seconds()
        is_immediately = (past <= 120)
        if is_immediately:
            print("[flashnews]execute immediately")
            instance.send_date = now
            call_execute_news(instance)
        else:
            print("[flashnews]notify_news_change: " + str(instance.send_date) + " out of date,drop it")
        # 如果已经存在该job 删除掉
        job = news_in_scheduler.get(instance.id)
        if job:
            job.Remove()
        return

    job = news_in_scheduler.get(instance.id)
    if not job:
        insert_news_of_notice(instance)
        print('insert_news_of_notice')
    else:
        scheduler.reschedule_job(job.id, trigger='date', run_date=instance.send_date)
        print('modify_news_of_notice')


def notify_news_delete(sender, instance, **kwargs):
    job = news_in_scheduler.get(instance.id)
    if not job:
        print("error:job not created but delete?")
        return
    job.remove()


init_scheduler_from_database()
signals.post_save.connect(notify_news_change, sender=FlashNewsRecord)
signals.post_delete.connect(notify_news_delete, sender=FlashNewsRecord)
