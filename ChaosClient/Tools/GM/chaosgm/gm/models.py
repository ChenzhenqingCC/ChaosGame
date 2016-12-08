# coding=utf-8
import json
import os
import urllib2

from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField
from django.utils import timezone
import chaosgm.settings
from django.conf import settings
from functools import wraps
import random
from django.conf import settings
from django.utils.decorators import available_attrs
import hashlib
from openpyxl import load_workbook


class TimezoneMiddleware(object):
    def process_request(self, request):
        if not hasattr(request.user, 'gm'):
            timezone.deactivate()
            return
        gm = request.user.gm
        if gm.timezone is None:
            timezone.deactivate()
            return
        timezone.activate(gm.timezone)


# 游戏服务器
class Server(models.Model):
    server_id = models.CharField(max_length=30)
    name = models.CharField(max_length=128)
    ip = models.CharField(max_length=128)
    port = models.CharField(max_length=10)
    intranet = models.CharField(max_length=128)
    dir = models.CharField(max_length=128)
    os_type = models.IntegerField()
    wx_os_type = models.IntegerField()
    db = models.CharField(max_length=128)
    db_oss = models.CharField(max_length=128)
    db_slave = models.CharField(max_length=128)
    db_oss_slave = models.CharField(max_length=128)

    def __getitem__(self, key):
        return getattr(self, key)

    def __unicode__(self):
        return self.name


class META:
    ordering = ['name']  # 公告服务器组


class ServerGroup(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class GM(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manage_server_groups = models.ManyToManyField(ServerGroup)
    timezone = TimeZoneField(default=chaosgm.settings.TIME_ZONE)


def http_req_server(obj, id_server):
    json_str = json.dumps(obj)
    rsp = None
    f = None
    try:
        server = Server.objects.get(id=id_server)
        port = int(server.port) + settings.GM_PORT_ADD
        url = u"http://{0}:{1}/gm".format(server.ip, port)

        req = urllib2.Request(url, json_str, {'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        rsp = json.load(f, encoding='utf8')
        print("send " + url + " rsp " + str(rsp))
    except Exception, e:
        print e
    finally:
        if f:
            f.close()
    return rsp


def QueryFromGMServer(obj, id_server, ignore_ret=False):
    rsp = http_req_server(obj, id_server)
    if rsp is not None and (ignore_ret or rsp['return'] == 1):
        return rsp
    else:
        return None


def Send2GMServer(obj, id_server):
    rsp = http_req_server(obj, id_server)
    ret = "404"
    if rsp is not None:
        ret = rsp['return']
    return ret


if hasattr(random, 'SystemRandom'):
    randrange = random.SystemRandom().randrange
else:
    randrange = random.randrange
_MAX_CSRF_KEY = 18446744073709551616L  # 2 << 63


def _get_new_submit_key():
    return hashlib.md5("%s%s" % (randrange(0, _MAX_CSRF_KEY), settings.SECRET_KEY)).hexdigest()


def anti_resubmit(page_key=''):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(self, request, *args, **kwargs):
            if request.method == 'GET':
                request.session['%s_submit' % page_key] = _get_new_submit_key()
                print 'session:' + request.session.get('%s_submit' % page_key)
            elif request.method == 'POST':
                old_key = request.session.get('%s_submit' % page_key, '')
                if old_key == '':
                    from django.http import HttpResponseForbidden
                    return HttpResponseForbidden('dupplicate post')
                request.session['%s_submit' % page_key] = ''
            return view_func(self, request, *args, **kwargs)

        return _wrapped_view

    return decorator


class GameXlsxTable():
    TYPE_ROW = 1

    def __init__(self, xlsx_file_name, sheet_name):
        wb = load_workbook(filename=os.path.join(settings.BASE_DIR, xlsx_file_name))
        sheet_ranges = wb[sheet_name]
        all_rows = sheet_ranges.rows
        type_row = all_rows[self.TYPE_ROW]
        if not type_row:
            raise Exception("no type row")

        types = [col.value for col in type_row]

        rows = []
        self.rows = rows
        for i in range(self.TYPE_ROW + 1, len(all_rows)):
            row = {}
            iter_row = all_rows[i]
            index = 0
            for col in iter_row:
                row[types[index]] = col.value
                index += 1
            rows.append(row)

    def Find(self, type, value):
        for row in self.rows:
            if row[type] == value:
                return row


item_table = None
