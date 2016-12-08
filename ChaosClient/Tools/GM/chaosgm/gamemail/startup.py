# coding=utf-8
from django.db.models import signals

from models import clear_mail_lock
from models import init_scheduler_from_database
from models import notify_news_delete
from models import GameMailRecordGroup



clear_mail_lock()
init_scheduler_from_database()
signals.post_delete.connect(notify_news_delete, sender=GameMailRecordGroup)
