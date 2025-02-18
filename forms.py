from django import forms
from .models import Lead, Appointment, PhoneCall

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'contact_info', 'address', 'email', 'status', 'notes']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['lead', 'appointment_date', 'location', 'notes']

class PhoneCallForm(forms.ModelForm):
    class Meta:
        model = PhoneCall
        fields = ['date', 'duration', 'notes', 'outcome']
