from rest_framework import generics
from .models import Lead
from .serializers import LeadSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

# Home view
def home(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    if request.method == "POST":
        # Get username and password from the form
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        # Check if user is valid
        if user is not None:
            login(request, user)  # Log the user in
            return HttpResponseRedirect(reverse('home'))  # Redirect to the home page after successful login
        else:
            # If login fails, render the login page with an error message
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    
    # If it's a GET request, just render the login page
    return render(request, 'login.html')

# Lead List View (API)
class LeadListView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

# Lead Detail View (API)
class LeadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
