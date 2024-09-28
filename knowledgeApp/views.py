from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from knowledgeApp.models import QA
from knowledgeApp.serializers import QASerializer  # 接下来将创建的序列化器

class QAListView(generics.ListAPIView):
    queryset = QA.objects.all()
    serializer_class = QASerializer
