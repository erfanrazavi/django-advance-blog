from django.urls import path , include
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken





app_name = "api-v1"



urlpatterns = [
    #registration
    path("registration/" , RegistrationApiView.as_view() , name="registration"),
    
    #change password
    #reset password
    #login token
    path('token/login/', CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),

    #login jwt
    
]   