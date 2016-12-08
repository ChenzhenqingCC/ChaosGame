from django.shortcuts import render
from gm.views import login
import util
import os
import datetime
from django.utils import timezone
from notice.models import NoticeRecord
from django.views.generic import ListView, View
from django.http import HttpResponseRedirect

# Create your views here.
def notice(request):
    if not request.user.is_authenticated():
        return login(request)

    if request.method == 'POST':
        content = request.POST.get('notice_content', '')
        query_name = request.POST.get('hidden_query_name', '')
        if query_name is None:
            print("query_name is nil")
            return

        ret, reason = util.execute_notice(query_name, content)
        if ret:
            now = timezone.now()
            record = NoticeRecord.objects.create(result=reason, author=request.user.username, content=content,
                                                 create_date=now, send_date=now, server_group=query_name, sended=True)
            record.save()
            return render(request, 'notice_send.html', {})
        else:
            names = util.get_notice_names(request)
            rsp_content = {
                'active_menu': 'notice',
                'user': request.user,
                'notice_names': names,
                'query_name': query_name,
                'content_list': content,
                'error': reason,
            }
            return render(request, 'notice.html', rsp_content)

    names = util.get_notice_names(request)
    query_name = request.GET.get('query_name', names[0])
    content_list = util.get_notice_content(query_name)
    content = {
        'active_menu': 'notice',
        'user': request.user,
        'notice_names': names,
        'query_name': query_name,
        'content_list': content_list,
    }
    return render(request, 'notice.html', content)


def notice_list(request):
    if not request.user.is_authenticated():
        return login(request)
    request.session['admin_entry'] = "/notice"
    request.session.modified = True
    return HttpResponseRedirect('/admin/notice/noticerecord/')
