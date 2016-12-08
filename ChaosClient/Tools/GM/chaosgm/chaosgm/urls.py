from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles import views
from django.conf import settings

js_info_dict = {
    'packages': ('js_locale/jscripti18n',),
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('gm.urls')),
    url(r'', include('notice.urls')),
    url(r'', include('ban.urls')),
    url(r'', include('flashnews.urls')),
    url(r'', include('account.urls')),
    url(r'', include('gamemail.urls')),
    url(r'', include('server.urls')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.static.serve, {'document_root': settings.STATIC_ROOT}, name="static"),
        url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
    ]
