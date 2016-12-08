# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from gm.models import GM
from gm.models import Server



class FlashNewsRecord(models.Model):
    gm = models.ForeignKey(GM, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    send_date = models.DateTimeField()
    servers = models.ManyToManyField(Server)
    sended = models.BooleanField(default=False)
    result = models.CharField(max_length=1000, null=True, blank=True)


