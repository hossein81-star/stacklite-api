from rest_framework import status
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (UserRegisterSerializer,CustomTokenObtainPairSerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView



class RegisterAPI(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)



class CustomObtainAuthToke(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

