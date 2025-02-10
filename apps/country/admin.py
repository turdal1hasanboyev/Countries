from django.contrib import admin

from .models import Country


class CountryAdmin(admin.ModelAdmin):
    """
    Admin interface for Country model.
    """
    list_display = (
        'uuid',
        'name',
        'iso_code',
        'capital',
        'population',
        'area',
        'continent',
        'currency',
        'phone_code',
        'leader_name',
        'leader_title',
        'flag',
        'is_active',
        'created_at',
        'updated_at',
    )
    ordering = ('name',)
    readonly_fields = (
        'uuid',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'continent',
    )
    search_fields = (
        'name',
        'iso_code',
        'capital',
        'continent',
        'currency',
        'phone_code',
        'leader_name',
        'leader_title',
    )
    
    fieldsets = (
        ('General', {
            'fields': ('name', 'iso_code', 'capital',),
        }),
        ('Geography', {
            'fields': ('population', 'area', 'continent',),
        }),
        ('Economy', {
            'fields': ('currency', 'phone_code',),
        }),
        ('Flag', {
            'fields': ('flag',),
        }),
        ('Politics', {
            'fields': ('leader_name', 'leader_title',),
        }),
        ('Permission', {
            'fields': ('is_active',),
        }),
        ('Important Dates', {
            'fields': ('created_at', 'updated_at',),
        }),
        ('UUID', {
            'fields': ('uuid',),
        }),
    )


admin.site.register(Country, CountryAdmin)
