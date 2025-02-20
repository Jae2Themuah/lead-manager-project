from django.urls import path
from .views import (
    HelloWorld, root_route, RegisterView, LoginView,
    LeadListCreate, LeadDetailView,
    AppointmentListCreate, PhoneCallListCreate
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

    # Phone Call Endpoints
    path("phone-calls/", PhoneCallListCreate.as_view(), name="phone-call-list"),
]
