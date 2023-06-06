from django.contrib import admin
from django.urls import path 
from django.urls import include, re_path
from django.conf.urls.static import static

from django.conf import settings

from Game import views
from .views import BNC, check, get_csrf


urlpatterns = [
    path('', views.StartGame, name='start'),
    path('game/', views.BNC, name='game'),
    path('check/',views.check_out, name='check'),
    path('getcsrf/', views.get_csrf, name = 'csrf'),
    path('win/', views.win, name='win'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)