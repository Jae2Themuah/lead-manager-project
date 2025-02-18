# myapp/urls.py
from django.urls import path
from . import views  # Ensure this imports the views correctly

urlpatterns = [
    path('', views.home, name='home'),  # Ensure you don't have a recursive view
]
