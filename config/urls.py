from django.contrib import admin
from django.urls import path, include  # Include allows linking to app-specific urls.py

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('myapp.urls')),  # Include URLs from myapp
]
