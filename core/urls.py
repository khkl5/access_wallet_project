from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("bookings/", views.booking_list_view, name="booking_list"),
    path("bookings/<int:pk>/", views.booking_detail_view, name="booking_detail"),
]