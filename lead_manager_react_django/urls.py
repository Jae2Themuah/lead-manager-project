from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # If you have API-specific URLs
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),  # Changed the name from '' to 'home/'
    path('auth/', include('authentication.urls')),  # Include authentication URLs
    path('add/', views.add_lead, name='add_lead'),
    path('edit/<int:pk>/', views.edit_lead, name='edit_lead'),
    path('myapp/', include('myapp.urls')),  # If you have URLs for 'myapp'
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login to get access & refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Get a new access token using refresh token
    path('api/', include('myapp.urls')),

    # JWT Token Views
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
