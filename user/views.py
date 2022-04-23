from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .serializers import CartSerializer, UserSerializer

from rest_framework_simplejwt.views import TokenViewBase
from .serializers import TokenObtainSerializer, TokenRefreshSerializer

# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class UserDetail(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    # pass

class CartCreate(generics.CreateAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TokenObtainPairView(TokenViewBase):
    """
        Return JWT tokens (access and refresh) for specific user based on username and password.
    """
    serializer_class = TokenObtainSerializer


class TokenRefreshView(TokenViewBase):
    """
        Renew tokens (access and refresh) with new expire time based on specific user's access token.
    """
    serializer_class = TokenRefreshSerializer