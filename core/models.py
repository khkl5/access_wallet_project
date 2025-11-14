from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    نموذج المستخدم الأساسي للنظام.
    يتيح مستقبلاً إضافة أدوار وصلاحيات (مدير، موظف، عميل...).
    """
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('staff', 'Staff')],
        default='staff'
    )

    def __str__(self):
        return self.username

class Booking(models.Model):
    guest = models.ForeignKey("guests.Guest", on_delete=models.CASCADE, related_name="bookings")
    room = models.CharField(max_length=50)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.guest.full_name} - {self.room}"