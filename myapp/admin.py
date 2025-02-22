from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Lead, PhoneCall, Appointment

# Register the custom User model
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Role', {'fields': ('role',)}),  # Ensure role is inside fieldsets
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(Lead)
admin.site.register(PhoneCall)
admin.site.register(Appointment)
