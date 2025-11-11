from django.contrib import admin
from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    """
    عرض وإدارة بيانات النزلاء في لوحة التحكم.
    """
    list_display = ('name', 'phone', 'unit_number', 'check_in', 'check_out', 'created_at')
    list_filter = ('unit_number', 'check_in', 'check_out')
    search_fields = ('name', 'phone', 'unit_number')
    ordering = ('-created_at',)