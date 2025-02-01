from rest_framework import generics

from .serializers import (RegistrationSerializer ,
                           CustomAuthTokenSerializer ,
                             CustomTokenObtainPairSerializer ,
                               ChangePasswordSerializer ,
                                 ProfileSerializer ,
                                        ActivationResendSerializer,  )

from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from ...models import Profile 
from django.shortcuts import get_object_or_404
# from django.core.mail import send_mail
from mail_templated import send_mail , EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()
import jwt
from jwt.exceptions import *
from django.conf import settings


class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request , *args, **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {
                'email' : email,
                'message' : 'User created successfully'
            }
            user_obj = get_object_or_404(User , email= email)
            token = self.get_tokens_for_user(user_obj)
            print(token , user_obj.email)

            email_obj = EmailMessage('email/activation_email.tpl', {'token': token}, 'erfan6235@gmail.com', to = [email])
            # send_mail('email/hello.tpl', {'user': self.user}, self.from_email, [self.user.email])
            EmailThread(email_obj).start() 
                       
            return Response(data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def get_tokens_for_user(self , user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
        

class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class CustomDiscardAuthToken(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordApiView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    model = User

    def get_object(self , queryset = None):
        obj = self.request.user
        return obj
    
    def put(self,request , *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status' : 'success',
                'message' : 'Password updated successfully',
                'code' : status.HTTP_200_OK,
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileApiView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset , user=self.request.user)
        return obj
    
class TestEmailApiView(generics.GenericAPIView):
    def get(self , request , *args , **kwargs):
        self.email = "hos@gmail.com"
        
        user_obj = get_object_or_404(User , email=self.email)
        token = self.get_tokens_for_user(user_obj)

        email_obj = EmailMessage('email/hello.tpl', {'token': token}, 'erfan6235@gmail.com', to = [self.email])
        # send_mail('email/hello.tpl', {'user': self.user}, self.from_email, [self.user.email])
        EmailThread(email_obj).start()
        return Response('email sent')
    
    def get_tokens_for_user(self , user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
class ActivationApiView(APIView):
   
    def get(self , request ,token ,  *args, **kwargs):
        
        # this code explain how to verify the token
            try:
                decoder = jwt.decode(token , settings.SECRET_KEY  ,  algorithms=['HS256'])
                user_id = decoder['user_id']
            
            except ExpiredSignatureError:
                return Response('token is expired')
            except DecodeError:
                return Response('token is invalid')
            except InvalidTokenError:
                return Response('token is invalid')
            
            
            
            user_obj = get_object_or_404(User , id = user_id)
            if user_obj.is_verified:
                return Response({'message' : 'your account have already been verified'})
            user_obj.is_verified = True 
            user_obj.save()               
            
            
            return Response({'message' : 'your account have been activated successfully'})
    
   
        
class ActivationResendApiView(generics.GenericAPIView):
    serializer_class = ActivationResendSerializer
    def post(self , request , *args , **kwargs):
            serializer = ActivationResendSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            user_obj = serializer.validated_data['user']
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation_email.tpl', {'token': token}, to = [user_obj.email])
            EmailThread(email_obj).start()
            return Response({'detail' : 'successfully sent to your email , please check your email1!'}, status = status.HTTP_200_OK) 
        
        
    def get_tokens_for_user(self , user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
   
        

   