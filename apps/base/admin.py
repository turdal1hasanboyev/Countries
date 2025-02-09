from django.contrib import admin

from .models import SubEmail


@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    """
    Admin interface for SubEmail model.
    """
    ordering = (
        'id',
    )
    list_display = (
        'id',
        'email',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )

    fieldsets = (
        (None, {
            'fields': ('email',),
        }),
        ('Permission', {
            'fields': ('is_active',),
        }),
        ('Date', {
            'fields': ('created_at', 'updated_at'),
        }),
        ('ID', {
            'fields': ('id',),
        }),
    )
