from django.urls import  path
from .views import RegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", obtain_auth_token, name= "login")
]
