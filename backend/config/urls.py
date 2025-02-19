from django.contrib import admin
from django.urls import path, include
from myapp.views import RegisterView, LoginUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', RegisterView.as_view(), name='register'),  # Register endpoint
    path('auth/login/', LoginUser.as_view(), name='login'),  # Login endpoint
    path('auth/', include('rest_framework.urls')),  # If using DRF authentication
]
