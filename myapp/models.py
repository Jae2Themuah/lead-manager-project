from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# myapp/models.py

#from django.contrib.auth.models import AbstractUser
#from django.db import models


# Define choices for lead status
LEAD_STATUS_CHOICES = [
    ('new', 'New'),
    ('contacted', 'Contacted'),
    ('qualified', 'Qualified'),
    ('closed', 'Closed'),
]

# Define choices for phone call dispositions
PHONE_CALL_DISPOSITION_CHOICES = [
    ('interested', 'Interested'),
    ('not_interested', 'Not Interested'),
    ('follow_up', 'Follow Up'),
    ('voicemail', 'Voicemail'),
    ('no_answer', 'No Answer'),
]

# Define choices for phone call outcome
PHONE_CALL_OUTCOME_CHOICES = [
    ('successful', 'Successful'),
    ('unsuccessful', 'Unsuccessful'),
    ('follow_up_needed', 'Follow-up Needed'),
]


class CustomUser(AbstractUser):
    """Extend the default Django User model with custom fields if necessary."""
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('agent', 'Agent'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=255, blank=True, null=True)
    #role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    
    def __str__(self):
        return self.username

class Lead(models.Model):
    """Model for tracking leads in the system"""
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email'), unique=True)
    phone = models.CharField(_('phone'), max_length=20)
    address = models.CharField(_('address'), max_length=255, blank=True)
    status = models.CharField(
        _('status'),
        max_length=50,
        choices=LEAD_STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    notes = models.TextField(_('notes'), blank=True, null=True)
    assigned_to = models.ForeignKey(
        CustomUser,  # Changed from User to CustomUser
        on_delete=models.SET_NULL,
        related_name='assigned_leads',
        null=True,
        blank=True,
        verbose_name=_('assigned to')
    )

    class Meta:
        verbose_name = _('lead')
        verbose_name_plural = _('leads')
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_full_contact_info(self):
        return f"Phone: {self.phone}, Email: {self.email}"

class PhoneCall(models.Model):
    """Model for tracking phone calls made to leads"""
    lead = models.ForeignKey(
        Lead, 
        related_name='phone_calls', 
        on_delete=models.CASCADE,
        verbose_name=_('lead')
    )
    date = models.DateTimeField(_('date'), auto_now_add=True)
    duration = models.DurationField(_('duration'))
    notes = models.TextField(_('notes'), blank=True, null=True)
    outcome = models.CharField(_('outcome'), max_length=50, choices=PHONE_CALL_OUTCOME_CHOICES)
    disposition = models.CharField(
        _('disposition'),
        max_length=20, 
        choices=PHONE_CALL_DISPOSITION_CHOICES, 
        null=True, 
        blank=True
    )
    made_by = models.ForeignKey(
        CustomUser,  # Changed from User to CustomUser
        on_delete=models.SET_NULL,
        related_name='phone_calls',
        null=True,
        blank=True,
        verbose_name=_('made by')
    )

    class Meta:
        verbose_name = _('phone call')
        verbose_name_plural = _('phone calls')
        ordering = ['-date']

    def __str__(self):
        return f"Phone Call for {self.lead.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"

    def get_duration_in_minutes(self):
        return self.duration.total_seconds() / 60

class Appointment(models.Model):
    """Model for scheduling appointments with leads"""
    APPOINTMENT_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
        ('rescheduled', 'Rescheduled'),
    ]
    
    lead = models.ForeignKey(
        Lead, 
        related_name='appointments', 
        on_delete=models.CASCADE,
        verbose_name=_('lead')
    )
    appointment_date = models.DateTimeField(_('appointment date'))
    location = models.CharField(_('location'), max_length=255)
    status = models.CharField(
        _('status'),
        max_length=50,
        choices=APPOINTMENT_STATUS_CHOICES,
        default='scheduled'
    )
    notes = models.TextField(_('notes'), blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser,  # Changed from User to CustomUser
        on_delete=models.SET_NULL,
        related_name='created_appointments',
        null=True,
        blank=True,
        verbose_name=_('created by')
    )
    assigned_to = models.ForeignKey(
        CustomUser,  # Changed from User to CustomUser
        on_delete=models.SET_NULL,
        related_name='assigned_appointments',
        null=True,
        blank=True,
        verbose_name=_('assigned to')
    )

    class Meta:
        verbose_name = _('appointment')
        verbose_name_plural = _('appointments')
        ordering = ['-appointment_date']

    def __str__(self):
        return f"Appointment for {self.lead.name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

    def get_status_display(self):
        return dict(self.APPOINTMENT_STATUS_CHOICES).get(self.status, 'Unknown')