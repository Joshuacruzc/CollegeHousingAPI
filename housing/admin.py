from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from housing.models import Housing, Owner, Image
from tags.admin import TagInline


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Housing)
class HousingAdmin(OSMGeoAdmin):
    list_display = ('address', 'owner')
    readonly_fields = []
    fields = ['address', 'owner', 'location', 'rent', 'bedrooms', 'bathrooms', 'spaces_available', 'description', 'gender',
              'availability_date']
    inlines = [
        TagInline,
        ImageInline,
    ]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
