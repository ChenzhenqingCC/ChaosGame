from django.conf.urls import patterns, url
import views

urlpatterns = [
	url(r'^server', views.ServerView.as_view(), name='server'),
]
