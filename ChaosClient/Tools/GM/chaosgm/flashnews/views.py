# coding=utf-8
from django.contrib.admin.widgets import AdminSplitDateTime, FilteredSelectMultiple
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.utils import timezone
from django.views.generic import View

from flashnews.models import FlashNewsRecord
from gm.views import login
from gm.models import Server
from django.contrib import messages
from django import forms
import time


class FlashNewsViewForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=100)
    send_date = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',)
        }

    def __init__(self, *args, **kwargs):
        super(FlashNewsViewForm, self).__init__(*args, **kwargs)
        servers = Server.objects.all()
        server_list = []
        for sv in servers:
            server_list.append((sv.id, sv.name))
        server_group_choice = tuple(server_list)

        self.fields['server'] = forms.MultipleChoiceField(choices=server_group_choice,
                                                          widget=FilteredSelectMultiple("服务器", is_stacked=False))
        for key in self.fields:
            self.fields[key].required = True


class FlashNewsView(View):
    def get(self, request, *args, **kwargs):
        form = FlashNewsViewForm()
        return render(request, 'flashnews/flashnews.html', {'form': form, 'active_menu': "flashnews"})

    def post(self, request, *args, **kwargs):
        form = FlashNewsViewForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['message']
            send_date = form.cleaned_data['send_date']
            server_ids = form.cleaned_data['server']

            servers = []
            for iter_id in server_ids:
                server = Server.objects.get(id=iter_id)
                servers.append(server)

            print(form.cleaned_data)
            now = timezone.now()
            record = FlashNewsRecord.objects.create(gm=request.user.gm, content=content, create_date=now, result='-',
                                                    send_date=send_date, sended=False)
            record.save()
            for iter_id in server_ids:
                server = Server.objects.get(id=iter_id)
                record.servers.add(server)
            record.save()
            messages.info(request, '执行成功')
            return HttpResponseRedirect('/flashnews')
        else:
            return render(request, 'flashnews/flashnews.html', {'form': form, 'active_menu': "flashnews"})


class FlashNewsList(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return login(request)
        request.session['admin_entry'] = "/flashnews"
        request.session.modified = True
        return HttpResponseRedirect('/admin/flashnews/flashnewsrecord/')
