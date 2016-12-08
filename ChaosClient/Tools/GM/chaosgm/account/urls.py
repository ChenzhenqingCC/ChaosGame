from django.conf.urls import patterns, url
import views

urlpatterns = [
	url(r'^account$', views.AccountView.as_view(), name='account'),
	#url(r'^query_game_account', views.QueryGameAccount.as_view(), name='query_game_account'),
]
