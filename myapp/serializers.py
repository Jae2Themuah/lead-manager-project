from rest_framework import serializers
from django.contrib.auth.models import User  # Import User model
from .models import Lead, Appointment, PhoneCall

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Add fields you need

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    lead = LeadSerializer()  # Nested lead serializer if needed
    class Meta:
        model = Appointment
        fields = '__all__'

class PhoneCallSerializer(serializers.ModelSerializer):
    lead = LeadSerializer()  # Nested lead serializer if needed
    class Meta:
        model = PhoneCall
        fields = '__all__'
