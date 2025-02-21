from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import LeadListView, LeadDetailView
from django.shortcuts import render
from . import views

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    # JWT Token Views
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # Lead views
    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),

    # Other views
    path('login/', views.login_view, name='login'),
    path('', home, name='home'),  # Make sure this points to your home page view
]
