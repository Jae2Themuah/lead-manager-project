from django.contrib import admin
from .models import Lead, Appointment, PhoneCall

# Register your models
admin.site.register(Lead)
admin.site.register(Appointment)
admin.site.register(PhoneCall)