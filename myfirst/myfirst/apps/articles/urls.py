from django.urls import path
from django.conf.urls import include
from . import views


app_name = 'articles'
urlpatterns = [
	path('speaking_club', views.speakingClub, name = 'speakingClub'), 
	path('', views.index, name = 'index'),
	path('universities', views.unv, name = 'unv'),
	path('universities/<int:article_unv_id>/', views.detail_unv, name = 'detail_unv'),
	path('toefl', views.toefl, name = 'toefl'),
	path('toefl/<int:article_toefl_id>/', views.detail_toefl, name = 'detail_toefl'),
	path('tipsandlifehacks', views.tal, name = 'tal'),
	path('tipsandlifehacks/<int:article_tal_id>/', views.detail_tal, name = 'detail_tal'),
	path('<int:articleId>/', views.detail, name = 'detail'),
	path('grappelli/', include('grappelli.urls'))
]

