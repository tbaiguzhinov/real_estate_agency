from django.contrib import admin

from .models import Flat, Likes_And_Complaints

class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner",)
    readonly_fields = ("created_at",)
    list_display = ("address", "price", "new_building", "construction_year", "town",)
    list_editable = ("new_building",)
    list_filter = ("new_building","rooms_number", "has_balcony", "active",)
    raw_id_fields = ("likes",)

class Likes_And_ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "flat",)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Likes_And_Complaints, Likes_And_ComplaintsAdmin)