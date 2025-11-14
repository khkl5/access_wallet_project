from django.contrib import admin
from .models import AccessPass


@admin.register(AccessPass)
class AccessPassAdmin(admin.ModelAdmin):
    list_display = ("id", "booking", "pass_id", "is_active", "created_at", "expires_at")
    list_filter = ("is_active", "created_at", "expires_at")
    search_fields = ("pass_id", "booking__id")
    readonly_fields = ("created_at",)