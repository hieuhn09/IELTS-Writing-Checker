from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('user-login', views.user_login, name='user-login'),
    path('user-register', views.user_register, name='user-register'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('profile', views.profile, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)