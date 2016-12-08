# coding=utf-8
from __future__ import unicode_literals

from django.db import models
import chaosgm.settings
from django.db.models import signals
from scheduler import scheduler
import util
from django.utils import timezone


# Create your models here.


class NoticeRecord(models.Model):
    author = models.CharField(max_length=128)
    content = models.CharField(max_length=chaosgm.settings.MAX_NOTICE_LEN)
    create_date = models.DateTimeField()
    send_date = models.DateTimeField()
    server_group = models.CharField(max_length=128)
    sended = models.BooleanField(default=False)
    result = models.CharField(max_length=128, null=True, blank=True)

    def get_aware_senddate(self):
        # zone = timezone.get_default_timezone_name()
        # pytz.timezone(zone).localize(self.send_date)
        return self.send_date

    class META:
        ordering = ['send_date']

    def __unicode__(self):
        return str(self.send_date)

