from django import forms
from .models import Lead
from django.core.exceptions import ValidationError
import re

class LeadForm(forms.ModelForm):
    # Custom validation for the phone number field
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        error_messages={'required': 'Phone number is required.'}
    )
    
    # Custom validation for the email field
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
        error_messages={'invalid': 'Please enter a valid email address.'}
    )

    # Address field with more detailed validation (optional address format)
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Enter address'}),
        required=False,
        error_messages={'max_length': 'Address is too long, limit to 255 characters.'}
    )

    # Status field with choices, making sure the value is valid
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('converted', 'Converted'),
        ('lost', 'Lost'),
    ]
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'status-select'}),
        error_messages={'required': 'Please select a status.'}
    )

    # Notes field with custom validation
    notes = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Add any notes here...'}),
        required=False,
        max_length=500,
        error_messages={'max_length': 'Notes are too long, limit to 500 characters.'}
    )

    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'address', 'status', 'notes']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Ensure the phone number is in a valid format (basic example, can be more complex)
            if not re.match(r'^\+?1?\d{9,15}$', phone):
                raise ValidationError('Phone number must be in a valid format (+1234567890).')
        return phone

    def clean_address(self):
        address = self.cleaned_data.get('address')
        # Check if the address has a minimum length (could be customized further)
        if address and len(address) < 5:
            raise ValidationError('Address should be at least 5 characters long.')
        return address

    def clean(self):
        # Custom form-wide validation (e.g., check if the email is in the correct domain, etc.)
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        
        # Example: Ensure email domain is one of the approved domains
        if email:
            allowed_domains = ['example.com', 'domain.com']
            email_domain = email.split('@')[-1]
            if email_domain not in allowed_domains:
                raise ValidationError(f"Email domain must be one of the following: {', '.join(allowed_domains)}")
        
        return cleaned_data

    def save(self, commit=True):
        # Custom save behavior (can log, alter data before saving, etc.)
        instance = super().save(commit=False)
        # Example: Automatically assign a user to a lead (if applicable)
        # instance.user = some_user_logic()
        if commit:
            instance.save()
        return instance
