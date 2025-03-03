from django.contrib import admin
from .models import Appointment, Lead, PhoneCall, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.conf import settings

# Register the custom User model
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Display fields in the user list view
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('role', 'is_staff', 'is_active')

    # Add fields to the form layout for creating/editing users
    fieldsets = (
        (None, {'fields': ('username', 'password')}),  # Basic user credentials
        ('Personal Information', {'fields': ('first_name', 'last_name', 'email')}),  # Personal details
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),  # Permissions
        ('Role', {'fields': ('role',)}),  # Custom role for user (admin, manager, etc.)
        ('Date Information', {'fields': ('date_joined', 'last_login')}),  # Track dates
    )

    # Add fields when creating a new user (for the "Add" form)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_active')}), 
    )

    ordering = ('username',)  # Default ordering of the users in the list view

    class Media:
        css = {
            'all': ('css/admin_custom.css',)  # Ensure you have the custom CSS file in your static folder
        }
        js = ('js/admin_custom.js',)  # Custom JS for enhanced interactivity (e.g., dynamic UI)

# Inline editing for related models (PhoneCall, Appointment)
class PhoneCallInline(admin.TabularInline):
    model = PhoneCall
    extra = 1  # How many empty forms to show by default in the inline
    fields = ('date', 'duration', 'outcome', 'disposition', 'made_by', 'notes')
    readonly_fields = ('date',)

class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 1
    fields = ('appointment_date', 'location', 'status', 'assigned_to', 'notes')
    readonly_fields = ()  # Removed readonly_fields to allow editing

# Lead model in the admin
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'status', 'assigned_to', 'created_at')
    list_filter = ('status', 'created_at', 'assigned_to')
    search_fields = ('name', 'email', 'phone', 'notes')
    ordering = ('-created_at',)  # Order by creation date (newest first)
    inlines = [PhoneCallInline, AppointmentInline]
    
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'address', 'status', 'assigned_to')
        }),
        ('Additional Information', {
            'fields': ('notes',),
            'classes': ('collapse',),
        }),
    )

    # Custom action for marking leads as contacted
    def mark_as_contacted(self, request, queryset):
        """Custom admin action to mark leads as contacted"""
        queryset.update(status='contacted')
        self.message_user(request, "Selected leads marked as contacted")

    mark_as_contacted.short_description = 'Mark selected leads as contacted'

    # Add the action to the LeadAdmin class
    actions = ['mark_as_contacted']

@admin.register(PhoneCall)
class PhoneCallAdmin(admin.ModelAdmin):
    list_display = ('lead', 'date', 'duration', 'outcome', 'disposition', 'made_by')
    list_filter = ('outcome', 'disposition', 'date', 'made_by')
    search_fields = ('lead__name', 'notes')
    date_hierarchy = 'date'
    
    fieldsets = (
        (None, {
            'fields': ('lead', 'duration', 'outcome', 'disposition', 'made_by')
        }),
        ('Additional Information', {
            'fields': ('notes',),
            'classes': ('collapse',),
        }),
    )

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('lead', 'appointment_date', 'location', 'status', 'assigned_to', 'created_by')
    list_filter = ('status', 'appointment_date', 'assigned_to', 'created_by')
    search_fields = ('lead__name', 'lead__email', 'location', 'notes')
    date_hierarchy = 'appointment_date'
    
    fieldsets = (
        (None, {
            'fields': ('lead', 'appointment_date', 'location', 'status', 'assigned_to')
        }),
        ('Additional Information', {
            'fields': ('notes', 'created_by'),
            'classes': ('collapse',),
        }),
    )