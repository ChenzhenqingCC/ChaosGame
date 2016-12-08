from django.conf.urls import patterns, url
import views

urlpatterns = [
	url(r'^gamemail$', views.GameMailView.as_view(), name='gamemail'),
	url(r'^gamemail_send$', views.gamemail_send, name='gamemail_send'),
	url(r'^gamemail_list$', views.GameMailListView.as_view(), name='gamemail_list'),
	url(r'^gamemail_del$', views.gamemail_del, name='gamemail_del'),
	url(r'^gamemail_resend$', views.gamemail_resend, name='gamemail_resend'),
	url(r'^gamemail_validate$', views.gamemail_validate, name='gamemail_validate'),
]
