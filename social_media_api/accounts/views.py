from django.shortcuts import render
from .serializers import UserRegistrationSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = []  # Allow unauthenticated access
