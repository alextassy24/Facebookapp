from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id', 'email', 'phone_number', 'password', 
            'first_name', 'last_name', 'date_of_birth'
        )

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {"email": f"An account with the email '{value}' already exists."})
        return value

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                {"phone_number": f"An account with the phone number '{value}' already exists."})
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid email or password")
        return data
