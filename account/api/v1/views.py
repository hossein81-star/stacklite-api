from django.contrib.auth import get_user_model
from rest_framework import status
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (UserRegisterSerializer, CustomTokenObtainPairSerializer, ChangePasswordSerializer,
                          ResetPasswordSerializer,ResetPasswordConfirmSerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
token_generator = PasswordResetTokenGenerator()
User = get_user_model()


class RegisterAPI(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomObtainAuthToke(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserLogOutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)

        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPI(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ResetPasswordAPI(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

        # reset_link = f"http://localhost:8000/account/api/v1/password-reset-confirm/?uid={uid}&token={token}"
            reset_link = f"http://localhost:8000/account/api/v1/password-reset-confirm/{uid}/{token}/"

            send_mail(

                subject=f"{user.email} Password Reset---UID:{uid}---Token:{token}",
                message=f"Reset your password: {reset_link}",
                from_email="noreply@example.com",
                recipient_list=[email],
            )
        except User.DoesNotExist:
            pass
        return Response(
            {"message": "If the email exists, a reset link has been sent."},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer

    def post(self, request,uid,token):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_password = serializer.validated_data["new_password"]

        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except:
            return Response({"error": "Invalid UID"}, status=400)

        if not token_generator.check_token(user, token):
            return Response({"error": "Invalid token"}, status=400)

        user.set_password(new_password)
        user.save()

        return Response({"message": "Password reset successful"})


