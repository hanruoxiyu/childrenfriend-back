from django.shortcuts import render
# views.py
from rest_framework import generics
from .models import Score
from .serializers import ScoreSerializer

class ScoreListView(generics.ListAPIView):
    queryset = Score.objects.all()  # 查询所有Score记录
    serializer_class = ScoreSerializer  # 使用上面定义的序列化器
