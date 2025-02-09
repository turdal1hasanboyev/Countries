from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin interface for Contact model.
    """
    ordering = (
        '-id',
    )
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'message',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'email',
        'name',
        'phone_number',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )

    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone_number', 'message',),
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
