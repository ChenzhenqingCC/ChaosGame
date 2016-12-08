# coding=utf-8
from django.contrib.admin.widgets import AdminSplitDateTime, FilteredSelectMultiple

from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import View

from gm.views import login
from gm.models import Server
from django.contrib import messages
from models import *
from django import forms
import json
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.decorators.cache import never_cache
from gm.models import anti_resubmit
from gm.models import item_table
from gm.models import QueryFromGMServer


class GameMailViewForm(forms.Form):
    send_date = forms.SplitDateTimeField(widget=AdminSplitDateTime())
    title = forms.CharField(widget=forms.TextInput, required=True, max_length=72)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=420)

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',)
        }

    def __init__(self, *args, **kwargs):
        super(GameMailViewForm, self).__init__(*args, **kwargs)
        servers = Server.objects.all()
        server_list = []
        for sv in servers:
            server_list.append((sv.id, sv.name))
        server_group_choice = tuple(server_list)

        self.fields['server_list'] = forms.MultipleChoiceField(choices=server_group_choice,
                                                               widget=FilteredSelectMultiple("服务器", is_stacked=False))
        for key in self.fields:
            self.fields[key].required = True


class GameMailView(View):
    @anti_resubmit(page_key='GameMailView')
    @never_cache
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)
        form = GameMailViewForm()
        return render(request, 'gamemail/gamemail.html', {'form': form, 'active_menu': "gamemail"})

    @anti_resubmit(page_key='GameMailView')
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)
        form = GameMailViewForm(request.POST)
        if form.is_valid():
            send_date = form.cleaned_data['send_date']
            server_ids = form.cleaned_data['server_list']
            title = form.cleaned_data['title']
            content = form.cleaned_data['message']

            accounts = request.POST.get('accounts', '')
            is_whole_accounts = (request.POST.get('whole_accounts', '') == u'on')
            if not is_whole_accounts and accounts == u'':
                return HttpResponseForbidden()

            now = timezone.now()
            record = GameMailRecordGroup.objects.create(gm=request.user.gm, title=title, content=content,
                                                        is_to_whole_accounts=is_whole_accounts, create_date=now,
                                                        send_date=send_date, sended=False)
            record.save()
            # mails
            for iter_id in server_ids:
                server = Server.objects.get(id=iter_id)
                mail = GameMailRecord.objects.create(server=server, group=record)
                mail.save()
            # accs
            hidden_items_json = request.POST.get('hidden_items', '')
            hidden_items = json.loads(hidden_items_json, encoding='utf8')
            for item in hidden_items:
                acc = GameMailAccRecord.objects.create(item_id=item.get(u'item_id'), num=item.get(u'num'),
                                                       item_type=item.get(u'item_type'),
                                                       group=record)
                acc.save()
            # targets
            target_accounts = accounts.split(",")
            for account in target_accounts:
                target = GameMailTargetAccountRecord.objects.create(account=account, group=record)
                target.save()

            on_mailgroup_create(record)
            return HttpResponseRedirect('/gamemail_send')
        return render(request, 'gamemail/gamemail.html', {'form': form, 'active_menu': "gamemail"})


def gamemail_send(request):
    return render(request, 'gamemail/gamemail_send.html', {})


def gamemail_del(request):
    mail_group_id = request.GET.get('mail_group_id')
    page = request.GET.get('page')
    if mail_group_id is None or page is None:
        return HttpResponseForbidden("error params")
    mail_group = GameMailRecordGroup.objects.get(id=int(mail_group_id))
    if mail_group is None:
        messages.error("该邮件不存在")
        return HttpResponseRedirect('/gamemail_list?page=' + page)
    if mail_group.sended:
        return HttpResponseForbidden("can't delete sended mails")
    mail_group.delete()
    messages.success(request, '删除成功')
    # url = reverse('gamemail_list', kwargs={'page': page})
    return HttpResponseRedirect('/gamemail_list?page=' + page)


def gamemail_resend(request):
    mail_id = request.POST.get('mail_id', '')
    if mail_id == '':
        return HttpResponseForbidden("error params")
    mail = GameMailRecord.objects.get(id=int(mail_id))
    resend_mail(mail)
    response_data = {'state': mail.get_state_html(), 'op': mail.get_state_icon_html()}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_account_info(infos, id):
    for info in infos:
        if info['id'] == id:
            return info


def gamemail_validate(request):
    need_check_str = request.POST.get('need_check', '')
    servers_str = request.POST.get('servers', '')
    if need_check_str == '':
        return HttpResponseForbidden("error params")
    if servers_str == '':
        return HttpResponseForbidden("error params")

    need_checks = json.loads(need_check_str, encoding='utf8')
    servers = json.loads(servers_str, encoding='utf8')

    error_list = []
    info_list = []
    accounts = None
    for check in need_checks:
        if check[u'type'] == u'item':
            item = check[u'value']
            if item[u'item_type'] == u'item':
                item_id = int(item[u'item_id'])
                item_info = item_table.Find(u'id', item_id)
                if item_info:
                    info_list.append({u'type': u'item', u'value': item_info})
                else:
                    error_list.append({u'type': u'item_not_exist', u'value': item})
        elif check[u'type'] == u'accounts':
            accounts = check[u'value']

    if accounts is not None and len(accounts) != 0:
        if len(servers) > 1:
            return HttpResponseForbidden("error params")
        account_ids = [int(account['id']) for account in accounts]
        obj = {'msg_id': 'actors_brief', 'rid_list': account_ids}
        accounts_info = QueryFromGMServer(obj, servers[0]['id'], True)
        for info in accounts_info:
            info_list.append({u'type': u'account', u'value': info})

        for id in account_ids:
            info = get_account_info(accounts_info, id)
            if info is None:
                error_list.append({u'type': u'account_not_exist', u'value':{u'id':id}})

        response_data = {u'error_list': error_list, u'info_list': info_list}
        rsp = json.dumps(response_data)
        return HttpResponse(rsp, content_type="application/json")

class GameMailListView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)

        limit = 15  # 每页显示的记录数
        groups = GameMailRecordGroup.objects.order_by('-send_date')
        paginator = Paginator(groups, limit)  # 实例化一个分页对象

        page = request.GET.get('page', 1)  # 获取页码
        try:
            ret = paginator.page(page)  # 获取某页对应的记录
        except PageNotAnInteger:  # 如果页码不是个整数
            ret = paginator.page(1)  # 取第一页的记录
        except EmptyPage:  # 如果页码太大，没有相应的记录
            ret = paginator.page(paginator.num_pages)  # 取最后一页的记录

        return render(request, 'gamemail/gamemail_list.html', {'page': ret, 'active_menu': "gamemail"})
