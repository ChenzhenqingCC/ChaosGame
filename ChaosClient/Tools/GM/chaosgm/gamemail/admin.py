from django.contrib import admin
from models import *


# Register your models here.
class GameMailRecordInline(admin.StackedInline):
    model = GameMailRecord
    can_delete = False


class GameMailRecordGroupAdmin(admin.ModelAdmin):\
    inlines = (GameMailRecordInline,)


admin.site.register(GameMailRecordGroup, GameMailRecordGroupAdmin)
