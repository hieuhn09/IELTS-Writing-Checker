from django.urls import path
from . import views

urlpatterns = [
    path('check', views.writting_checker, name='writting-checker'),
    path('history', views.writting_history, name='writting-history'),
]