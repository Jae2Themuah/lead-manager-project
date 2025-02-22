from django.http import JsonResponse
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes

from .models import Lead, Appointment, PhoneCall
from .serializers import LeadSerializer, AppointmentSerializer, PhoneCallSerializer

User = get_user_model()

def get_tokens_for_user(user):
    """Generate JWT tokens for authentication."""
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

@login_required
def protected_endpoint(request):
    """Django login-required endpoint."""
    return JsonResponse({"message": "This is a protected endpoint"})

class JSONAPIView(APIView):
    """Base class with JSON renderer for API responses."""
    renderer_classes = [JSONRenderer]

def root_route(request):
    """Root route for API welcome message."""
    return JsonResponse({"message": "Welcome to the Lead Manager API!"})

class RegisterView(JSONAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """User registration endpoint."""
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not all([username, password, email]):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        tokens = get_tokens_for_user(user)

        return Response({"message": "User created successfully", "tokens": tokens}, status=status.HTTP_201_CREATED)

class LoginView(JSONAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """User login endpoint."""
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user:
            tokens = get_tokens_for_user(user)
            return Response({"message": "Login successful", "tokens": tokens}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class ProtectedView(JSONAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Protected route example."""
        return Response({"message": "You have accessed a protected route!"}, status=status.HTTP_200_OK)

class LeadListCreate(ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

class LeadDetailView(JSONAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Retrieve a single lead."""
        lead = get_object_or_404(Lead, pk=pk)
        serializer = LeadSerializer(lead)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Update a lead."""
        lead = get_object_or_404(Lead, pk=pk)
        serializer = LeadSerializer(lead, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a lead."""
        lead = get_object_or_404(Lead, pk=pk)
        lead.delete()
        return Response({"message": "Lead deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class AppointmentListCreate(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

class PhoneCallListCreate(ListCreateAPIView):
    queryset = PhoneCall.objects.all()
    serializer_class = PhoneCallSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

class PhoneCallDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PhoneCall.objects.all()
    serializer_class = PhoneCallSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def test_api(request):
    """Test API endpoint."""
    return Response({"message": "API is working!"})

class HelloWorld(JSONAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """Simple Hello World endpoint."""
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)

class DebugHeadersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Returns request headers for debugging purposes."""
        return JsonResponse({"headers": dict(request.headers)})
