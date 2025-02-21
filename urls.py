from django.contrib import admin
from django.urls import path, include
from .views import protected_endpoint

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),  # Include authentication URLs
    path('protected-endpoint/', protected_endpoint, name='protected-endpoint'),
]