from django.http import JsonResponse
from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from django.contrib.auth.decorators import login_required
from .models import Lead, Appointment, PhoneCall
from .serializers import LeadSerializer, AppointmentSerializer, PhoneCallSerializer
from django.views import View
from django.http import HttpResponse



User = get_user_model()


def get_tokens_for_user(user):
    """Generate JWT tokens for authentication."""
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


# Protecting the root route with login_required
@login_required
def protected_endpoint(request):
    """Django login-required endpoint."""
    return JsonResponse({"message": "This is a protected endpoint"})


# JSONAPIView base class with JSON renderer for API responses
class JSONAPIView(APIView):
    renderer_classes = [JSONRenderer]


def root_route(request):
    """Root route with basic API information and dynamic data."""
    try:
        num_leads = Lead.objects.count()
        num_appointments = Appointment.objects.count()
        num_phone_calls = PhoneCall.objects.count()
        message = "API is up and running"
    except Exception as e:
        message = f"Error: {str(e)}"

    api_info = {
        "message": message,
        "status": "API is operational",
        "total_leads": num_leads,
        "total_appointments": num_appointments,
        "total_phone_calls": num_phone_calls,
        "endpoints": {
            "GET /api/leads/": "List all leads",
            "POST /api/leads/": "Create a new lead",
            "GET /api/leads/<id>/": "Get a specific lead",
            "POST /api/register/": "Register a new user",
            "POST /api/login/": "Login and get JWT tokens",
            "GET /api/protected/": "Access protected route (requires JWT token)",
        },
        "version": "v1.0",
    }
    return JsonResponse(api_info)


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


class LeadCreateView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]  # Protect this endpoint with authentication


class ProtectedView(JSONAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Protected route example."""
        return Response({"message": "You have accessed a protected route!"}, status=status.HTTP_200_OK)


class LeadListCreate(ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]  # Ensure this endpoint requires authentication
    renderer_classes = [JSONRenderer]


class LeadDetailView(JSONAPIView):
    permission_classes = [IsAuthenticated]  # Ensure this endpoint requires authentication

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
    permission_classes = [IsAuthenticated]  # Protect this endpoint with authentication
    renderer_classes = [JSONRenderer]


class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]  # Ensure this endpoint requires authentication
    renderer_classes = [JSONRenderer]


class PhoneCallListCreate(ListCreateAPIView):
    queryset = PhoneCall.objects.all()
    serializer_class = PhoneCallSerializer
    permission_classes = [IsAuthenticated]  # Protect this endpoint with authentication
    renderer_classes = [JSONRenderer]


class PhoneCallDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PhoneCall.objects.all()
    serializer_class = PhoneCallSerializer
    permission_classes = [IsAuthenticated]  # Ensure this endpoint requires authentication
    renderer_classes = [JSONRenderer]


@api_view(["GET"])
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
    permission_classes = [IsAuthenticated]  # Ensure this endpoint requires authentication

    def get(self, request):
        """Returns request headers for debugging purposes."""
        return JsonResponse({"headers": dict(request.headers)})


class SomeView(View):
    def get(self, request):
        return HttpResponse("This is SomeView")


class SomeOtherView(View):
    def get(self, request):
        return HttpResponse("This is SomeOtherView")

# Define example_view
def example_view(request):
    return JsonResponse({"message": "This is an example view"})