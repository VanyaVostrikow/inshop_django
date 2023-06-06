from django.contrib import admin
from django.urls import path 
from django.urls import include, re_path
from django.conf.urls.static import static

from django.conf import settings

from . import views


urlpatterns = [
    path('active/', views.coupon_apply, name ='apply'),
    path('create/',views.coupon_create_game, name='create_game'),
    path('search/',views.SearchCoupon, name="search"),
    path('searchbot/',views.SearchCouponBot, name="searchbot"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)