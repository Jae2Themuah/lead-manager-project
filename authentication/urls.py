from django.contrib import admin
from django.urls import path, include
from . import views
from authentication.views import RegisterView  # Add the RegisterView import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('authentication.urls')),  # Include authentication URLs here
    path('auth/register/', RegisterView.as_view(), name='register'),  # Ensure the registration path is correct
    path('', views.home, name='home'),
]
