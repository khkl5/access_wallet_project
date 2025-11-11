from django.contrib import admin
from .models import DoorPass


@admin.register(DoorPass)
class DoorPassAdmin(admin.ModelAdmin):
    """
    إدارة بطاقات الدخول المرتبطة بالنزلاء.
    """
    list_display = ('guest', 'serial', 'access_code', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('serial', 'access_code', 'guest__name', 'guest__phone')
    ordering = ('-created_at',)