from django.db import models
from django.utils import timezone
from guests.models import Booking


class AccessPass(models.Model):
    STATUS_CHOICES = [
        ('not_created', 'لم تُنشأ'),
        ('active', 'مفعّلة'),
        ('cancelled', 'ملغاة'),
        ('expired', 'منتهية'),
    ]

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name='access_pass'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_created'
    )
    wallet_pass_id = models.CharField(
        max_length=255,
        blank=True,
        help_text="المعرّف القادم من Apple Wallet أو نظام القفل"
    )
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_active(self):
        now = timezone.now()
        return (
            self.status == 'active'
            and self.valid_from
            and self.valid_to
            and self.valid_from <= now <= self.valid_to
        )

    def __str__(self):
        return f"AccessPass for Booking #{self.booking_id}"