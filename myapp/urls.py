from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    HelloWorld, 
    root_route, 
    RegisterView, 
    LoginView,
    LeadListCreate, 
    LeadDetailView,
    AppointmentListCreate, 
    AppointmentDetailView,
    PhoneCallListCreate, 
    PhoneCallDetailView,
    ProtectedView,
    test_api,
    DebugHeadersView
)

urlpatterns = [
    # Root and basic endpoints
    path('', root_route, name='root'),
    path('api/hello/', HelloWorld.as_view(), name='hello_world'),
    path('api/protected/', ProtectedView.as_view(), name='protected'),
    path('api/test/', test_api, name='test_api'),
    path('api/debug-headers/', DebugHeadersView.as_view(), name='debug-headers'),

    # Authentication endpoints
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('auth/', include('dj_rest_auth.urls')),  
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    # JWT Token Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Lead Endpoints
    path('api/leads/', LeadListCreate.as_view(), name='lead-list'),
    path('api/leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),

    # Appointment Endpoints
    path('api/appointments/', AppointmentListCreate.as_view(), name='appointment-list'),
    path('api/appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),

    # Phone Call Endpoints
    path('api/phone-calls/', PhoneCallListCreate.as_view(), name='phone-call-list'),
    path('api/phone-calls/<int:pk>/', PhoneCallDetailView.as_view(), name='phone-call-detail'),
]
