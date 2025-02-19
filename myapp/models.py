from django.db import models

# Define choices for lead status
LEAD_STATUS_CHOICES = [
    ('new', 'New'),
    ('contacted', 'Contacted'),
    ('qualified', 'Qualified'),
    ('closed', 'Closed'),
]

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=LEAD_STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Add a field for notes
    notes = models.TextField(blank=True, null=True)
    
    # Add phone call information
    phone_calls = models.ManyToManyField('PhoneCall', related_name='leads', blank=True)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    lead = models.ForeignKey(Lead, related_name='appointments', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    
    # Add phone call information related to the appointment
    phone_calls = models.ManyToManyField('PhoneCall', related_name='appointments', blank=True)
    
    def __str__(self):
        return f"Appointment for {self.lead.name} on {self.appointment_date}"

class PhoneCall(models.Model):
    date = models.DateTimeField()
    duration = models.DurationField(help_text="Duration in minutes")  # You can also use a TimeField or IntegerField
    notes = models.TextField(blank=True, null=True)
    outcome = models.CharField(max_length=100, choices=[
        ('successful', 'Successful'),
        ('unsuccessful', 'Unsuccessful'),
        ('follow-up', 'Follow-up Needed')
    ])
    
    def __str__(self):
        return f"Phone Call on {self.date}"
