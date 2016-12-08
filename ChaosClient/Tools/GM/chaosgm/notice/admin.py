from django.contrib import admin
from models import *
from django import forms
from django.utils import timezone
from pprint import pprint


class NoticeRecordForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 30, 'cols': 200}))
    create_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))
    send_date = forms.DateTimeInput()
    result = forms.CharField()

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(NoticeRecordForm, self).__init__(*args, **kwargs)
        user = request.user
        all_group = user.gm.manage_server_groups.all()
        notice_list = []
        for gr in all_group:
            notice_list.append((gr.name, gr.name))
        server_group_choice = tuple(notice_list)
        self.fields['server_group'] = forms.ChoiceField(choices=server_group_choice, initial='internal')

    class Meta:
        model = NoticeRecord
        fields = '__all__'


class NoticeRecordAdmin(admin.ModelAdmin):
    readonly_fields = ("sended", "result")
    list_display = ('author', 'sended', 'result', 'send_date', 'server_group', 'create_date')
    all_fields = ('author', 'sended', 'result', 'send_date', 'server_group', 'create_date','content')
    list_filter = ('author',)
    form = NoticeRecordForm
    date_hierarchy = 'send_date'
    list_per_page = 20

    def get_queryset(self, request):
        qs = super(NoticeRecordAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        if hasattr(request.user, 'gm'):
            gm = request.user.gm
            groups = list(gm.manage_server_groups.all())
            ret = qs.filter(server_group__in=groups)
            return ret

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.sended:
            return self.all_fields
        return self.readonly_fields

    def get_changeform_initial_data(self, request):
        out = super(NoticeRecordAdmin, self).get_changeform_initial_data(request)
        out['author'] = request.user.username
        out['create_date'] = timezone.now()
        return out

    def has_delete_permission(self, request, obj=None):
        ret = super(NoticeRecordAdmin, self).has_delete_permission(request,obj)
        if ret:
            if obj is not None:
                return not obj.sended
            else:
                return True
        return False

    def get_form(self, request, obj=None, **kwargs):
        AdminForm = super(NoticeRecordAdmin, self).get_form(request, obj, **kwargs)

        class AdminFormWithRequest(AdminForm):
            def __new__(cls, *args, **kwargs):
                kwargs['request'] = request
                return AdminForm(*args, **kwargs)

        return AdminFormWithRequest


admin.site.register(NoticeRecord, NoticeRecordAdmin)
