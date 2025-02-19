from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('auth/', include('authentication.urls')),
    path('add/', views.add_lead, name='add_lead'),
    path('edit/<int:pk>/', views.edit_lead, name='edit_lead'),
]
