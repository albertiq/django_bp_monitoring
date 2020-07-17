from django.urls import path
from django.urls import re_path
from . import views
from django.conf.urls import url
#from pacient_result.views import ArticleDetailView
from pacient_result.views import PacientDetail


urlpatterns = [

    path('dashboard/', views.index, name="dashboard"),
    url(r'^pacients/$', views.PacientList.as_view(), name='pacients'),
    path('dashboard/<pk>', PacientDetail.as_view(), name="pacient-detail"),
    url(r'^recomendation/create/$', views.Recomend_create.as_view(), name='recomend_create'),
    url(r'^recomendations/$', views.RecomendList.as_view(), name='recomends'),
    url(r'^recomendations_pacient/$', views.RecomendList_pacient.as_view(), name='recomends_pac'),
    #path('publishers/', ArticleListView.as_view()),

]
