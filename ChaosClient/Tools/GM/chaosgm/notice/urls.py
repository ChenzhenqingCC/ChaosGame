from django.conf.urls import patterns, url
import views

urlpatterns = [
	url(r'^notice$', views.notice, name='notice'),
	url(r'^notice_list$', views.notice_list, name='notice_list'),
]
