from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model



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

