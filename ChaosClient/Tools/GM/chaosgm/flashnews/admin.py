from django.contrib import admin
from models import *
from django import forms
from django.utils import timezone
from gm.models import Server


class FlashNewsRecordForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 200}))
    send_date = forms.DateTimeInput()
    result = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(FlashNewsRecordForm, self).__init__(*args, **kwargs)
        servers = Server.objects.all()
        servers_list = []
        for s in servers:
            servers_list.append((s.id, s.name))
        server_choice = tuple(servers_list)
        self.fields['server'] = forms.ChoiceField(choices=server_choice)

    class Meta:
        model = FlashNewsRecord
        fields = '__all__'


class  FlashNewsRecordAdmin(admin.ModelAdmin):
    readonly_fields = ("sended", "result")
    list_display = ('sended', 'result', 'send_date', 'processing_servers', 'create_date')
    all_fields = ('gm', 'content', 'create_date', 'send_date', 'servers', 'sended','result')
    #list_filter = ('author',)
    form = FlashNewsRecordForm
    date_hierarchy = 'send_date'
    list_per_page = 20

    def processing_servers(self,record):
        names = u''
        for sv in record.servers.all():
            names = names + sv.name + "; "
        return names

    processing_servers.short_description = 'servers'
    processing_servers.allow_tags = False

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.sended:
            return self.all_fields
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        ret = super(FlashNewsRecordAdmin, self).has_delete_permission(request,obj)
        if ret:
            if obj is not None:
                return not obj.sended
            else:
                return True
        return False


admin.site.register(FlashNewsRecord, FlashNewsRecordAdmin)