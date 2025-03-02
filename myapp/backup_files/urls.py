from django.urls import path
from .views import (
    HelloWorld, root_route, RegisterView, LoginView,
    LeadListCreate, LeadDetailView,
    AppointmentListCreate, AppointmentDetailView,  # Added missing AppointmentDetailView
    PhoneCallListCreate, PhoneCallDetailView,  # Added missing PhoneCallDetailView
)

urlpatterns = [
    path('api/hello/', HelloWorld.as_view(), name='hello_world'),
    path("", root_route, name="root"),  # Home Page
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),

    # Lead Endpoints
    path("leads/", LeadListCreate.as_view(), name="lead-list"),
    path("leads/<int:pk>/", LeadDetailView.as_view(), name="lead-detail"),

    # Appointment Endpoints
    path("appointments/", AppointmentListCreate.as_view(), name="appointment-list"),
    path("appointments/<int:pk>/", AppointmentDetailView.as_view(), name="appointment-detail"),

    # Phone Call Endpoints
    path("phone-calls/", PhoneCallListCreate.as_view(), name="phone-call-list"),
    path("phone-calls/<int:pk>/", PhoneCallDetailView.as_view(), name="phone-call-detail"),
]
