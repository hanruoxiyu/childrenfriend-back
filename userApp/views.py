from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from userApp.serializers import MyTokenObtainPairSerializer

# 登录接口
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# 注册接口
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        # 获取前端传入的信息
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        # 判断是否注册过
        if User.objects.filter(username=username).exists():
            return Response({'error': '该用户名已经存在.'}, status=400)
        if User.objects.filter(email=email).exists():
            return Response({'error': '该邮箱已经存在.'}, status=400)
        # 创建用户
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return Response({'message': '注册成功'},status=200)