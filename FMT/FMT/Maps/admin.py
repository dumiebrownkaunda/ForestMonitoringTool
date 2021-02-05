from django.contrib import admin
from .models import Areas, Countries
from leaflet.admin import LeafletGeoAdmin


class AreasAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
    list_per_page = 10


class CountrieAdmin(LeafletGeoAdmin):
    list_display = ('name', 'area', 'lat', 'lon', 'region')
    list_per_page = 10
    search_fields = ('name', 'area')
    ordering = ['name']
    list_filter = ('name', 'lat')


admin.site.register(Areas, AreasAdmin)
admin.site.register(Countries, CountrieAdmin)
