from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.site_header = "Countries Admin Paneli"
admin.site.site_title = "Countries Admin Paneli"
admin.site.index_title = "Countries Admin Paneliga xush kelibsiz!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom User Admin Model
    """
    ordering = ('id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'image',
        'is_staff',
        'is_superuser',
        'is_active',
        'last_login',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'last_login',
        "date_joined",
    )

    fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'description', 'image',),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Important Dates', {
            'fields': ('created_at', 'updated_at', "date_joined", 'last_login',),
        }),
        ('ID', {
            'fields': ('id',),
        }),
    )

    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
        ('Permissions', {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser',),
        }),
    )
