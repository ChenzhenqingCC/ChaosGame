from django.conf.urls import patterns, url
import views

urlpatterns = [
	url(r'^ban_edit$', views.BanEdit.as_view(), name='ban_edit'),
	url(r'^ban_list$', views.BanList.as_view(), name='ban_list'),
	#url(r'^query_game_account', views.QueryGameAccount.as_view(), name='query_game_account'),
]
