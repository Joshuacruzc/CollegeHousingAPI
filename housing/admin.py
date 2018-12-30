from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from housing.models import Housing


@admin.register(Housing)
class HousingAdmin(OSMGeoAdmin):
    list_display = ('')

