from django.urls import path
from . import views

app_name = 'guests'

urlpatterns = [
    path('bookings/', views.booking_list_view, name='booking_list'),
    # لاحقًا:
]
