from django.contrib import admin
from .models import AccessPass


@admin.register(AccessPass)
class AccessPassAdmin(admin.ModelAdmin):
    list_display = ("id", "booking", "status", "valid_from", "valid_to", "created_at")
    list_filter = ("status",)
    search_fields = ("booking__guest__full_name", "wallet_pass_id")