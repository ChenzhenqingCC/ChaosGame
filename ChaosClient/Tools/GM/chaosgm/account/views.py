# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from gm.models import QueryFromGMServer, Server
from django.utils import timezone
import datetime

class AccountView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account/account.html', {u'servers': Server.objects.all(),'active_menu': "account"})

    def post(self, request, *args, **kwargs):
        account = request.POST.get('account', '')
        name = request.POST.get('name', '')
        server = int(request.POST.get('server', ''))
        if name == '' and account == '':
            return HttpResponseRedirect('/account')

        if account != '':
            obj = {'msg_id': 'actor_info', 'actor_rid': int(account)}
        elif name!= '':
            obj = {'msg_id': 'actor_info', 'name': name}

        account_obj = QueryFromGMServer(obj,server)
        attrs = []
        if account_obj is not None:
            attrs.append({'name':'id','value':account_obj['id']})
            attrs.append({'name':'uin','value':account_obj['uin']})
            attrs.append({'name':'名字','value':account_obj['name']})
            attrs.append({'name':'战力','value':account_obj['gs']})
            attrs.append({'name':'等级','value':account_obj['level']})
            attrs.append({'name':'金币','value':account_obj['coin']})
            attrs.append({'name':'钻石','value':account_obj['diamond']})
            attrs.append({'name':'vip等级','value':account_obj['vip']})
            attrs.append({'name':'消费人民币','value':account_obj['rmb']})

            is_online = "否"
            if account_obj['online'] == 1:
                is_online = "是"
            attrs.append({'name':'是否在线','value':is_online})

            lasttime = timezone.make_aware( datetime.datetime.fromtimestamp(account_obj['lasttime']),request.user.gm.timezone)
            attrs.append({'name':'最后在线时间','value':str(lasttime)})
            attrs.append({'name':'渠道','value':account_obj['channel']})
        return render(request, 'account/account.html', {u'servers': Server.objects.all(),'active_menu': "account",'attr_list':attrs,'server_id':server})
