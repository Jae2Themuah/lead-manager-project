from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

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
    ('follow-up', 'Follow-up Needed'),
]

class User(AbstractUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('sales_rep', 'Sales Representative'),
        ('business_owner', 'Business Owner'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='sales_rep')

    # Fixing related_name conflicts with auth.User.groups
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
    )

    def __str__(self):
        return f"{self.username} - {self.role}"

class PhoneCall(models.Model):
    lead = models.ForeignKey('Lead', related_name='phone_calls', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(help_text="Duration as a time delta")
    notes = models.TextField(blank=True, null=True)
    outcome = models.CharField(max_length=50, choices=PHONE_CALL_OUTCOME_CHOICES)
    disposition = models.CharField(max_length=20, choices=PHONE_CALL_DISPOSITION_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Phone Call for {self.lead.name} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=LEAD_STATUS_CHOICES,
        default='new'
    )
    contact_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    lead = models.ForeignKey(Lead, related_name='appointments', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.lead.name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')}"

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)