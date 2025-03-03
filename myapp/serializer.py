from rest_framework import serializers
from .models import Lead
from django.core.exceptions import ValidationError
import re

class LeadSerializer(serializers.ModelSerializer):
    # You can add custom validations and extra fields if needed

    def validate_email(self, value):
        """
        Custom email validation to ensure it's in the correct format.
        """
        if '@' not in value:
            raise ValidationError("Email must contain '@'.")
        return value

    def validate_phone(self, value):
        """
        Custom phone number validation to ensure it follows a valid format.
        This example expects phone numbers to be in the format (XXX) XXX-XXXX.
        """
        phone_regex = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
        if not phone_regex.match(value):
            raise ValidationError("Phone number must be in the format (XXX) XXX-XXXX.")
        return value

    class Meta:
        model = Lead
        fields = '__all__'

    def validate(self, data):
        """
        Custom overall validation to check any additional requirements.
        """
        if 'status' not in data or not data['status']:
            raise ValidationError("Status is required.")
        return data

    # If needed, you can add extra fields or custom methods here:
    # Example: Additional fields that are not part of the model but are calculated
    # extra_field = serializers.CharField(source='get_calculated_field', read_only=True)
