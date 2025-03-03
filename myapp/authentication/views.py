from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # Logic for login
        return Response({"message": "Login successful"})

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        # Logic for registration
        return Response({"message": "Registration successful"})
