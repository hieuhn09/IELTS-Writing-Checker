from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('user-login', views.user_login, name='user-login'),
    path('user-register', views.user_register, name='user-register'),
    path('user-logout', views.user_logout, name='user-logout'),
]