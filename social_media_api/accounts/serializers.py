from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only = True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
    
    def validate(self, attrs):
        # attrs (attributes) contain the cleaned data, it returns the data after field-level validation.
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'Error': 'password do not match'})
        return super().validate(attrs)
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        return data

    