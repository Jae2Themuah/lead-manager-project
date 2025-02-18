from django.urls import path
from .views import LeadListView, LeadDetailView
from django.shortcuts import render
from . import views

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('login/', views.login_view, name='login'),
    path('', home, name='home'),  # Make sure this points to your home page view
]
