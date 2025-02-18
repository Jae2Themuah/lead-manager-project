from django.urls import path
from . import views  # Assuming views is where your login function is

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', views.login_view, name='login'),  # Add this line
    path('', views.home, name='home'),
]
