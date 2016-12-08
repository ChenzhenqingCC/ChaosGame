from django.conf.urls import patterns, url
import views

urlpatterns = [
	url(r'^flashnews$', views.FlashNewsView.as_view(), name='flashnews'),
	url(r'^flashnews_list$', views.FlashNewsList.as_view(), name='flashnews_list'),
]
