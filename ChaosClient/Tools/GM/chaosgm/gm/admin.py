from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from models import *
# Register your models here.
class GMInline(admin.StackedInline):
    model = GM
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (GMInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ServerGroupAdmin(admin.ModelAdmin):
    list_display = ('name','url')

class ServerAdmin(admin.ModelAdmin):
    list_display = ('server_id','name','ip','port')

admin.site.register(ServerGroup)
admin.site.register(Server,ServerAdmin)