from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):

    User = get_user_model()

    model = User
    fields = ["id", "username", "email", "password", "profile_picture", "bio"]

    extra_kwargs ={
        'password' : {'write_only' : True}
    }


    def create(self, validated_data):

        User = get_user_model()

        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user) # Create token automatically
        return user
