from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check, name='core_health'),
    
]