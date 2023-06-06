from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import include


urlpatterns = [
    path('', views.FeedbackFormView.as_view(), name = 'main'), 
    path("success/", views.SuccessView.as_view(), name="success"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
