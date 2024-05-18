from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('result', views.result, name='writting-result'),
    path('history', views.writting_history, name='writting-history'),
    path('public', views.public_writting, name='public-writting'),
    path('toggle-public', views.toggle_public, name='toggle-public'),
    path('download_doc', views.download_doc, name='download_doc'),

]