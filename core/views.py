# core/views.py
# core/views.py
from django.shortcuts import render, get_object_or_404
from guests.models import Booking  # بدل .modelscore.models

def booking_list_view(request):
    bookings = Booking.objects.select_related("guest").all()
    return render(request, "booking_list.html", {"bookings": bookings})


def booking_detail_view(request, pk):
    booking = get_object_or_404(
        Booking.objects.select_related("guest"),
        pk=pk,
    )
    return render(request, "booking_detail.html", {"booking": booking})