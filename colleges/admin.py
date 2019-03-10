from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from colleges.models import College


@admin.register(College)
class CollegeAdmin(OSMGeoAdmin):
    list_display = ('name',)
    fields = ['name', 'location']