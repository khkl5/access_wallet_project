from core.models import Booking
from django.db import models
from core.models import Booking


class AccessPass(models.Model):
    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="access_pass",
        help_text="الحجز المرتبط بهذه البطاقة",
    )
    pass_id = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text="معرف البطاقة في النظام أو في Apple Wallet (إن وجد)",
    )
    wallet_url = models.URLField(
        blank=True,
        null=True,
        help_text="رابط تحميل البطاقة في المحفظة",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="وقت إنشاء البطاقة",
    )
    expires_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="وقت انتهاء صلاحية البطاقة إن وجد",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="هل البطاقة مفعّلة الآن؟",
    )

    class Meta:
        verbose_name = "Access Pass"
        verbose_name_plural = "Access Passes"

    def __str__(self):
        if self.pass_id:
            return f"Pass {self.pass_id} for booking {self.booking_id}"
        return f"Pass for booking {self.booking_id}"