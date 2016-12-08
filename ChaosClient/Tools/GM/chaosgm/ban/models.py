from __future__ import unicode_literals

from django.db import models
from gm.models import GM


class BanRecord(models.Model):
    account = models.CharField(max_length=128)
    account_name = models.CharField(max_length=128, null=True)
    account_zone = models.CharField(max_length=128, null=True)
    reason = models.CharField(max_length=128, null=True, blank=True)
    time = models.BigIntegerField()
    type = models.CharField(max_length=128)
    gm = models.ForeignKey(GM, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField()
    ret = models.CharField(max_length=128)
    class META:
        ordering = ['create_date']

    def __unicode__(self):
        return str(self.create_date)