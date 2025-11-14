# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from core.models import Booking
def booking_list_view(request):
    bookings = Booking.objects.select_related("guest").all()
    return render(request, "booking_list.html", {"bookings": bookings})


def booking_detail_view(request, pk):
    booking = get_object_or_404(
        Booking.objects.select_related("guest"),
        pk=pk,
    )
    return render(request, "booking_detail.html", {"booking": booking})

def booking_create_view(request):
    """Create a new booking and redirect to its detail page when saved."""
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # After creating the booking, redirect to the detail view
            return redirect("core:booking_detail", pk=booking.pk)
    else:
        form = BookingForm()

    return render(request, "booking_form.html", {"form": form})