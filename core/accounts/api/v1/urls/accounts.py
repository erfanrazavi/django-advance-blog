from django.urls import path , include
from ..views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView , TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView




urlpatterns = [
    #registration
    path("registration/" , RegistrationApiView.as_view() , name="registration"),
    
    #change password
    path('change-password/' , ChangePasswordApiView.as_view() , name = 'change-password'),
    #reset password
    #login token
    path('token/login/', CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),

    #login jwt
    path('jwt/create/' , CustomTokenObtainPairView.as_view() , name="jwt-create"),
    path('jwt/refresh/' , TokenRefreshView.as_view() , name="jwt-refresh"),
    path('jwt/verify/' , TokenVerifyView.as_view() , name="jwt-verify"),

    
]   