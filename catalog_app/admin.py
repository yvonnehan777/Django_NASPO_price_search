from django.contrib import admin
from .models import NASPOItem

@admin.register(NASPOItem)
class NASPOItemAdmin(admin.ModelAdmin):
    list_display = ("vendor", "description", "manufacturer_part_number", "list_price", "naspo_price")
    search_fields = ("vendor", "description", "manufacturer_part_number")
    list_filter = ("vendor",)          # optional: quick filter by vendor
    ordering = ("vendor", "manufacturer_part_number")
    list_per_page = 50
