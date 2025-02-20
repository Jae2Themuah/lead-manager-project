from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Lead, Appointment, PhoneCall
from .serializers import LeadSerializer, AppointmentSerializer, PhoneCallSerializer
from rest_framework.views import APIView
from rest_framework import status
# Root route
def root_route(request):
    return HttpResponse("Welcome to the Lead Manager API!")

# Register User
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        if not username or not password or not email:
            return Response({"error": "Username, password, and email are required"}, status=400)
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)
        
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=400)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"message": "User created successfully"}, status=201)

# Login User
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=400)
        
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login successful"}, status=200)
        return Response({"error": "Invalid credentials"}, status=401)

# Lead Views
class LeadListCreate(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Lead Detail View (Fixing the error)
class LeadDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]

# Appointment Views
class AppointmentListCreate(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Phone Call Views
class PhoneCallListCreate(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        phone_calls = PhoneCall.objects.all()
        serializer = PhoneCallSerializer(phone_calls, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhoneCallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)