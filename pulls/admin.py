from django import forms
from django.contrib import admin
from .models import Pull, Tractor, Klass, Entry

# class EntryInline(admin.TabularInline):
#     model = Pull.entries.through

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('weight', 'name',)
        }),
    )

@admin.register(Pull)
class PullAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    list_display = ('name', 'date', 'class_count',)
    fieldsets = (
        (None, {
            'fields': ('name', 'date',),
        }),
        ('Classes', {
            'classes': ('collapse',),
            'fields': ('classes',),
        }),
    )
    filter_horizontal = ('classes',)
    # inlines = [EntryInline,]
    
@admin.register(Tractor)
class TractorAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass