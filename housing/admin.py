from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from housing.models import Housing, Owner


@admin.register(Housing)
class HousingAdmin(OSMGeoAdmin):
    list_display = ('address', 'owner')
    readonly_fields = []
    fields = ['address', 'owner', 'location']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

