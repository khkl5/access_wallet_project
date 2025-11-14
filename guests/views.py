from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.db.models import Prefetch

from .models import Booking
from passes.models import AccessPass


@login_required
@permission_required('guests.view_booking', raise_exception=True)
def booking_list_view(request):
    """
    واجهة الموظف/المدير لعرض جميع الحجوزات.
    """
    bookings = (
        Booking.objects
        .select_related('guest')
        .prefetch_related(
            Prefetch('access_pass', queryset=AccessPass.objects.all())
        )
        .all()
    )

    context = {
        'bookings': bookings,
    }
    return render(request, 'guests/booking_list.html', context)
