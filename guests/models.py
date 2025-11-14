from django.db import models
from django.conf import settings

class Guest(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.full_name


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد التأكيد'),
        ('confirmed', 'مؤكد'),
        ('cancelled', 'ملغى'),
    ]

    ROOM_CHOICES = [
        ('room1', 'Room 1'),
        ('room2', 'Room 2'),
        ('room3', 'Room 3'),
    ]

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='bookings')
    room = models.CharField(max_length=20, choices=ROOM_CHOICES)

    # تاريخ ووقت الدخول والخروج
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='confirmed'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_bookings'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-check_in', '-id']

    def __str__(self):
        return f'Booking #{self.id} - {self.guest} - {self.get_room_display()}'