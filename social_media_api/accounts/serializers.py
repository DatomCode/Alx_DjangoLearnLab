from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):

    model = get_user_model()
    fields = ["id", "username", "email", "password", "profile_picture", "bio"]

    extra_kwargs ={
        'password' : {'write_only' : True}
    }
    password = serializers.CharField()
    
    def create(self, validated_data):

        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user) # Create token automatically
        return user
