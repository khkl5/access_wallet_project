from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.db.models import Prefetch

from core.models import Booking
from passes.models import AccessPass

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from .models import Guest

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


@login_required
@permission_required('guests.add_booking', raise_exception=True)
def booking_create_view(request):
    if request.method == "POST":
        guest_name = (request.POST.get("guest_name") or "").strip()
        phone = (request.POST.get("phone") or "").strip()
        email = (request.POST.get("email") or "").strip()
        room = (request.POST.get("room") or "").strip()
        start_raw = request.POST.get("start_date") or ""
        end_raw = request.POST.get("end_date") or ""
        status = request.POST.get("status") or "confirmed"

        if not guest_name or not room or not start_raw or not end_raw:
            messages.error(request, "تأكدي من تعبئة الحقول المطلوبة.")
            return render(request, "guests/booking_create.html")

        start_dt = parse_datetime(start_raw)
        end_dt = parse_datetime(end_raw)

        if not start_dt or not end_dt:
            messages.error(request, "صيغة التاريخ غير صحيحة.")
            return render(request, "guests/booking_create.html")

        if end_dt <= start_dt:
            messages.error(request, "تاريخ الخروج يجب أن يكون بعد تاريخ الدخول.")
            return render(request, "guests/booking_create.html")

        guest, created = Guest.objects.get_or_create(
            full_name=guest_name,
            phone=phone,
            email=email,
        )

        Booking.objects.create(
            guest=guest,
            room=room,
            start_date=start_dt,
            end_date=end_dt,
            status=status,
        )

        messages.success(request, "تم إنشاء الحجز بنجاح.")
        return redirect("booking_list")

    return render(request, "guests/booking_create.html")