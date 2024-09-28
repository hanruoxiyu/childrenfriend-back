from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'id','username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
#     登录权限验证
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        token['email'] = user.email
        token['id'] = user.id
        return token
