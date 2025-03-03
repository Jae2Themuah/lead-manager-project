from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom user model extending the default AbstractUser model
class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django User model.
    Add custom fields like `phone_number`, `birth_date`, and `is_active` if necessary.
    """
    
    # Example: Add a phone number field
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name=_('Phone Number')
    )
    
    # Example: Add birth date field
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Birth Date')
    )
    
    # Optionally add any other fields to meet your business logic
    # Example: Add a field to manage user's membership status
    is_active_member = models.BooleanField(
        default=True,
        verbose_name=_('Is Active Member')
    )

    # Optionally add a profile picture or other fields
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        verbose_name=_('Profile Picture')
    )

    # Custom method to represent the user object
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Custom User')
        verbose_name_plural = _('Custom Users')
        ordering = ['username']
