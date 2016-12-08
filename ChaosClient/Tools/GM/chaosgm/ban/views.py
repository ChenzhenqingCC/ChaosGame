# coding=utf-8


from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from ban.models import BanRecord
from gm.views import login
from django.contrib import messages
from django.utils import timezone
from gm.models import Server
from gm.models import Send2GMServer


class BanEdit(View):
    ban_types = ["unban_chat", "ban_chat", "ban_login", "unban_login"]

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)

        return render(request, 'ban/ban_edit.html', {u'servers': Server.objects.all(), u'active_menu': u'ban_edit'})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)

        account = int(request.POST.get('account', ''))
        reason = request.POST.get('reason', '')
        hour = int(request.POST.get('time', ''))
        str_server = request.POST.get('server', '')
        id_server = int(str_server)
        second = hour * 60 * 60
        ban_type = request.POST.get('ban_type', '')

        if ban_type not in self.ban_types:
            return HttpResponseForbidden()

        obj = {'actor_rid': account, 'msg_id': ban_type, 'time': second}
        ret = Send2GMServer(obj, id_server)

        if ret == 1:
            messages.success(request, '发送成功')
            now = timezone.now()
            record = BanRecord.objects.create(ret=str(ret), account=str(account), reason=reason, time=second,
                                              create_date=now, type=ban_type, gm=request.user.gm)
            record.save()
        else:
            messages.warning(request, '发送失败，错误码:' + str(ret))

        return render(request, 'ban/ban_edit.html', {u'servers': Server.objects.all(), u'active_menu': u'ban_edit'})


class BanList(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)
        request.session['admin_entry'] = "/ban_edit"
        request.session.modified = True
        return HttpResponseRedirect('/admin/ban/banrecord/')

        # class QueryGameAccount(View):
        #     def post(self, request, *args, **kwargs):
        #         account = request.POST.get('account', '')
        #         game_name = request.POST.get('game_name', '')
        #         response_data = {}
        #         if account != '' or game_name != '':
        #
        #             req = urllib2.Request(settings.GM_SERVER,json_str, {'Content-Type': 'application/json'})
        #             f = urllib2.urlopen(req)
        #             rsp = json.load(f)
        #
        #         return HttpResponse(
        #             json.dumps(response_data),
        #             content_type="application/json"
        #         )
