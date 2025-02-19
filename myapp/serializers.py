from rest_framework import serializers
from .models import Lead, Appointment, PhoneCall

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class PhoneCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCall
        fields = '__all__'
