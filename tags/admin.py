from django.contrib import admin

from housing.models import Housing
from tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('description', )


class TagInline(admin.TabularInline):
    model = Housing.tags.through
