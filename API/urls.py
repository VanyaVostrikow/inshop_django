from django.contrib import admin
from django.urls import path 
from django.urls import include, re_path
from django.conf.urls.static import static

from django.conf import settings

from . import views


urlpatterns = [
    path('coupon/', views.api_coupon),
    path('coupon/<int:pk>/create/', views.api_create_coupon),
    path('coupon/<int:pk>/delete/', views.api_delete_coupon),
    path('coupon/<int:pk>/change/', views.api_change_coupon),
    path('coupon/<int:pk>/view/', views.api_view_coupon),


    path('order/<int:pk>/create/', views.api_create_order),
    path('order/<int:pk>/delete/', views.api_delete_order),
    path('order/<int:pk>/change/', views.api_change_order),
    path('order/<int:pk>/view/', views.api_view_order),

    path('user/create/',views.api_create_coupon),
    path('user/dekete/', views.api_delete_coupon),
    path('user/change/',views.api_change_coupon),
    path('user/view/',views.api_view_coupon),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)