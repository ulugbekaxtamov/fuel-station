from django.contrib import admin
from .models import Station, Fuel, Report


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude', 'is_open', 'is_available')
    search_fields = ('name',)
    list_filter = ('is_open', 'is_available')
    ordering = ('name',)


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('type', 'station', 'is_available', 'price', 'updated_at')
    search_fields = ('type', 'station__name')
    list_filter = ('type', 'is_available')
    autocomplete_fields = ('station',)
    ordering = ('-updated_at',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'fuel', 'is_available', 'price', 'created_at')
    search_fields = ('user__username', 'fuel__type', 'fuel__station__name')
    list_filter = ('is_available', 'fuel__type')
    autocomplete_fields = ('user', 'fuel')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
