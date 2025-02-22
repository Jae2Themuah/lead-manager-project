from django.contrib import admin
from django.urls import path, include

# Attempt to import the protected endpoint view
try:
    from myapp.views import protected_endpoint, DebugHeadersView  # type: ignore # Import protected view
except ImportError:
    protected_endpoint = None

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),  # Include authentication URLs
    path("api/", include("myapp.urls")),  # Include API URLs
    path("debug-headers/", DebugHeadersView.as_view(), name="debug-headers"),
]

# Add the protected endpoint only if it was successfully imported
if protected_endpoint:
    urlpatterns.append(
        path("protected-endpoint/", protected_endpoint, name="protected-endpoint")
    )