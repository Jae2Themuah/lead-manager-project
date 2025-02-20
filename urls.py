from django.contrib import admin
from django.urls import path
from myapp.views import RegisterView  # Import the view from your app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterView.as_view(), name="register"),
]
