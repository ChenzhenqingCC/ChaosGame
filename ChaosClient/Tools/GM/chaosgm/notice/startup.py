# coding=utf-8
from django.db.models import signals
from scheduler import scheduler
from django.utils import timezone
from multiprocessing.dummy import Pool
from gm.models import Send2GMServer
from models import NoticeRecord
import util


# 定时公告逻辑
def call_execute_notice(notice):
	ret, reason = util.execute_notice(notice.server_group, notice.content)
	notice.sended = True
	notice.result = reason
	notice.save()


notice_in_scheduler = {}


def insert_job_of_notice(notice):
	job = scheduler.add_job(call_execute_notice, 'date', run_date=notice.send_date, args=[notice])
	notice_in_scheduler[notice.id] = job


def init_scheduler_from_database():
	notices = NoticeRecord.objects.all()
	now = timezone.now()
	for notice in notices:
		if not notice.sended:
			send_date = notice.get_aware_senddate()
			if now > send_date:
				print("[notice]notice " + str(send_date) + " out of date,drop it")
			else:
				insert_job_of_notice(notice)
	scheduler.print_jobs()
	


# 监听写入或者删除noticerecord数据
def notify_notice_change(sender, instance, created, **kwargs):
	if instance.sended:
		return
	now = timezone.now()
	send_date = instance.get_aware_senddate()
	if now > send_date:
		# 如果在一分钟之内 视为立刻发送
		past = (now - send_date).total_seconds()
		is_immediately = (past <= 60)
		if is_immediately:
			print("[notice]execute notice immediately")
			instance.send_date = now
			call_execute_notice(instance)
		else:
			print("[notice]notify_notice_change: " + str(instance.send_date) + " out of date,drop it")
		# 如果已经存在该job 删除掉
		job = notice_in_scheduler.get(instance.id)
		if job:
			job.Remove()
		return

	if created:
		insert_job_of_notice(instance)
	else:
		job = notice_in_scheduler.get(instance.id)
		if not job:
			# 这种情况肯定是用户把一个已经过时的notice的发布时间调到将来了,重新插入job
			insert_job_of_notice(instance)
		else:
			scheduler.reschedule_job(job.id, trigger='date', run_date=instance.send_date)


def notify_notice_delete(sender, instance, **kwargs):
	job = notice_in_scheduler.get(instance.id)
	if not job:
		print("error:job not created but delete?")
		return
	job.remove()


init_scheduler_from_database()
signals.post_save.connect(notify_notice_change, sender=NoticeRecord)
signals.post_delete.connect(notify_notice_delete, sender=NoticeRecord)

# from datetime import datetime
# The job will be executed on November 6th, 2009 at 16:30:05



# def my_job(str):
#     global  t_job
#     t_job.modify(args=['haha2'])
#     print("hello world " + str)
#
# t_job = scheduler.add_job(my_job, 'interval', seconds = 2, args=['haha'])


# scheduler.add_job(my_job, 'date', run_date=datetime(2013, 1, 6, 16, 30, 5), args=['text'])
