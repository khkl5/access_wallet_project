from django.contrib import admin
from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    # نعرض فقط الـ id والنص اللي يرجعه __str__
    list_display = ("id", "__str__")
    # ترتيب بسيط بالـ id
    ordering = ("id",)
    # ما نستخدم list_filter على حقول غير مضمونة
    list_filter = ()
    search_fields = ()