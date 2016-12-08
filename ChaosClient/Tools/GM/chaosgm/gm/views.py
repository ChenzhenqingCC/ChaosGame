# coding=utf-8
import os

from django import forms
from django.contrib import auth
from django.contrib.admin.widgets import FilteredSelectMultiple, AdminSplitDateTime, AdminTimeWidget
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


# 定义表单模型
from django.views.generic import View


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名：')
    password = forms.CharField(label='密码：', widget=forms.PasswordInput())


# 登录
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('notice'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'login.html', content)


def index(request):
    if not request.user.is_authenticated():
        return login(request)
    user = request.user
    content = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'index.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))



