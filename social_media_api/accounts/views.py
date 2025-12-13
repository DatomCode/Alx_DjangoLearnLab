from django.shortcuts import render,get_object_or_404
from .serializers import UserRegistrationSerializer
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . models import CustomUser

# Create your views here.

User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = []  # Allow unauthenticated access


class ProfileView(generics.GenericAPIView):
    # Requirement: Use "generics.GenericAPIView" (inherited above)
    # Requirement: Use "permissions.IsAuthenticated"
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    def get(self, request, *args, **kwargs):
        # Simple logic to return the logged-in user's data
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if request.user == user_to_follow:
        return Response({"error": "Cannot follow yourself"}, status=400)
    request.user.following.add(user_to_follow)
    return Response({"message": "Followed successfully"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": "Unfollowed successfully"})