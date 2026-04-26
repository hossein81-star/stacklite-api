

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(max_length=255,write_only=True)
    password=serializers.CharField(max_length=255,write_only=True)

    class Meta:
        model = User
        fields = ['email','password','password1']

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

