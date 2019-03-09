from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from colleges.models import College
from housing.models import Image


@admin.register(College)
class CollegeAdmin(OSMGeoAdmin):
    list_display = ('name',)
    fields = ['name', 'location']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['image', 'Housing']
