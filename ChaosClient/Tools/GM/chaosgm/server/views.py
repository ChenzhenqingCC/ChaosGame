# coding=utf-8
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from gm.models import Server
from gm.views import login
from django.contrib import messages
from django import forms
import depoly_gm
import inspect

class ServerViewForm(forms.Form):
    op = forms.ChoiceField(
        choices=[('doStart', 'doStart'), ('doStop', 'doStop'), ('doFresh', 'doFresh'), ('doTar', 'doTar'),
                 ('hotfixCode', 'hotfixCode'), ('hotfixRes', 'hotfixRes'), ('monitor', 'monitor')])
    param = forms.CharField(widget=forms.TextInput())
    result = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 100, 'readonly': 'readonly'}))

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',)
        }

    def __init__(self, *args, **kwargs):
        super(ServerViewForm, self).__init__(*args, **kwargs)
        servers = Server.objects.all()
        server_list = []
        for sv in servers:
            server_list.append((sv.id, sv.name))
        server_group_choice = tuple(server_list)

        self.fields['server'] = forms.MultipleChoiceField(choices=server_group_choice,
                                                          widget=FilteredSelectMultiple("服务器", is_stacked=False))

        self.fields['op'].required = True
        self.fields['server'].required = True
        self.fields['param'].required = False
        self.fields['result'].required = False


class ServerView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)
        form = ServerViewForm()
        return render(request, 'server.html', {u'active_menu': u'server', u'form': form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)
        form = ServerViewForm(request.POST)
        if form.is_valid():
            op_id = form.cleaned_data['op']
            param = form.cleaned_data['param']
            server_ids = form.cleaned_data['server']
            servers = []
            for iter_id in server_ids:
                server = Server.objects.get(id=iter_id)
                servers.append(server)

            ret = eval('depoly_gm.'+op_id)(servers, param)
            form.result = ret
        return render(request, 'server.html', {u'active_menu': u'server', u'form': form})
