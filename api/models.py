from django.db import models

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'api'  # Explicitly associate this model with the 'api' app

    def __str__(self):
        return self.name
