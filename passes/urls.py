from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_list, name='passes_list'),
]