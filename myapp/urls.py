from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HelloWorld,
    root_route,
    RegisterView,
    LoginView,
    LeadListCreate,
    LeadDetailView,
    LeadCreateView,
    AppointmentListCreate,
    AppointmentDetailView,
    PhoneCallListCreate,
    PhoneCallDetailView,
    ProtectedView,
    test_api,
    DebugHeadersView,
    SomeView,  # Import SomeView
    SomeOtherView,  # Import SomeOtherView
    example_view,  # Import example_view
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# Ensure unique namespace for myapp
#app_name = 'myapp'

# Initialize the DefaultRouter and register any viewsets (optional, depending on your views)
router = DefaultRouter()
# router.register(r'leads', LeadViewSet)  # Example registration for viewsets if needed

urlpatterns = [
    # Root and basic endpoints
    path('', root_route, name='root'),
    path('api/hello/', HelloWorld.as_view(), name='hello_world'),
    path('api/protected/', ProtectedView.as_view(), name='protected'),
    path('api/test/', test_api, name='test_api'),
    path('api/debug-headers/', DebugHeadersView.as_view(), name='debug-headers'),

    # Include the router URLs for all viewsets registered with the DefaultRouter
    path('api/', include(router.urls)),

    # Authentication endpoints
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('auth/', include('dj_rest_auth.urls')),  
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    # JWT Token Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Lead Endpoints (class-based views)
    path('api/leads/', LeadListCreate.as_view(), name='lead-list'),
    path('api/leads/create/', LeadCreateView.as_view(), name='create-lead'),
    path('api/leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),

    # Appointment Endpoints
    path('api/appointments/', AppointmentListCreate.as_view(), name='appointment-list'),
    path('api/appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),

    # Phone Call Endpoints
    path('api/phone-calls/', PhoneCallListCreate.as_view(), name='phone-call-list'),
    path('api/phone-calls/<int:pk>/', PhoneCallDetailView.as_view(), name='phone-call-detail'),

    # Non-API views (for rendering non-API pages)
    path('leads/', LeadListCreate.as_view(), name='lead-list-create'),  # For non-API views related to leads

    # The views you wanted to keep
    path('some-view/', SomeView.as_view(), name='some-view'),
    path('some-other-view/', SomeOtherView.as_view(), name='some-other-view'),
    path('example/', example_view, name='example-view'),
]
