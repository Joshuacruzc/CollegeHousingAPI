from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from housing.models import Housing, Owner


@admin.register(Housing)
class HousingAdmin(OSMGeoAdmin):
    readonly_fields = ['image_tag']
    list_display = ('address', 'owner')
    fields = ['image_tag']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

