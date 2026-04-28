

from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ...models import Profile
User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(max_length=255,write_only=True)
    password=serializers.CharField(max_length=255,write_only=True)

    class Meta:
        model = User
        fields = ['email','password','password1','skills']

    def validate(self, attrs):
        password=attrs.get('password')
        password1=attrs.get('password1')
        if password!=password1:
            raise serializers.ValidationError('Password does not match')
        try:
            validate_password(password)


        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return attrs


    def create(self, validated_data):
        validated_data.pop('password1')
        return User.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data=super().validate(attrs)
        validated_data["email"]=self.user.email
        validated_data["user_id"]=self.user.id
        return validated_data

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password=serializers.CharField(write_only=True)
    new_password2=serializers.CharField(write_only=True)
    def validate(self, attrs):
        user = self.context['request'].user
        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError("Old password is not correct")
        if attrs["new_password"] != attrs["new_password2"]:
            raise serializers.ValidationError("passwords do not match")
        validate_password(attrs["new_password"])
        return attrs
    def save(self, **kwargs):
        self.validated_data.pop("new_password2")
        user = self.context['request'].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user



class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    def validate_email(self, value):
        return value



class ResetPasswordConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    def validate(self, data):
        new_password=data.get("new_password")
        password_confirmation=data.get("password_confirmation")
        if new_password != password_confirmation:
            raise serializers.ValidationError("Passwords do not match")
        validate_password(new_password)
        data.pop("password_confirmation")
        return data


class ActivationsResendSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    def validate(self,attrs):
        try:
            user=User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail":"user does not exist"})
        if user.is_verified:
            raise serializers.ValidationError({"detail":"user already verified"})
        attrs['user']=user
        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields=["username","bio","prof_image","expertise",]

