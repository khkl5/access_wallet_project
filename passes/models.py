from django.db import models
from guests.models import Guest
import uuid

class DoorPass(models.Model):
    """
    بطاقة دخول رقمية مرتبطة بنزيل.
    تحتوي على رقم تسلسلي ورمز يستخدمه النظام لاحقًا لتوليد pkpass.
    """
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='passes')
    serial = models.CharField(max_length=128, unique=True, default=uuid.uuid4)
    access_code = models.CharField(max_length=64)  # ممكن يكون رمز الباب أو كود خاص
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Pass for {self.guest.name} ({'Active' if self.is_active else 'Inactive'})"