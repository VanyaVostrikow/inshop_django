from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import include


urlpatterns = [
    path('', views.activate, name="activate"),
    path('code/', views.code, name="code"),
    path('check/', views.Check, name = "Check"),
    path('logintele/', views.LoginTele, name = "logintele"),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
