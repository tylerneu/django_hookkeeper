from django import forms
from django.contrib import admin
from .models import Pull, Tractor, Klass

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('weight', 'name',)
        }),
        (None, {
            'fields': ('tractors',)
        })
    )
    filter_horizontal = ('tractors',)

@admin.register(Pull)
class PullAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'class_count',)
    filter_horizontal = ('classes',)
    
@admin.register(Tractor)
class TractorAdmin(admin.ModelAdmin):
    pass
