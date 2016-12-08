# coding=utf-8
from django.contrib import admin
from models import BanRecord
import datetime
# Register your models here.
class BanRecordAdmin(admin.ModelAdmin):
    list_display = ('account', 'type', 'create_date','processing_enddate', 'processing_time','processing_gm','reason')
    list_display_links = None

    def processing_enddate(self,ban):
        if ban.time == 0:
            return '-'
        end_date = ban.create_date + datetime.timedelta(seconds=ban.time)
        return end_date

    processing_enddate.short_description = 'end_date'
    processing_enddate.allow_tags = False

    def processing_time(self,ban):
        if ban.time == 0:
            return '-'
        return ban.time/3600

    processing_time.short_description = 'hour'
    processing_time.allow_tags = False

    def processing_gm(self,ban):
        if ban.gm:
            return ban.gm.user.username
        return '-'

    processing_gm.short_description = 'gm'
    processing_gm.allow_tags = False

    # def __init__(self, *args, **kwargs):
    #     super(BanRecordAdmin, self).__init__(*args, **kwargs)
    #     self.list_display_links = (None, )

    date_hierarchy = 'create_date'
    list_per_page = 20

    def get_actions(self, request):
        #Disable delete
        actions = super(BanRecordAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False



admin.site.register(BanRecord, BanRecordAdmin)