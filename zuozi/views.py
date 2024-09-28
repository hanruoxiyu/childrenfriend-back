from django.shortcuts import render

from rest_framework import generics
from .models import ZuoZi
from .serializers import ZuoZiSerializer
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.views import View

class ZuoZiListAPIView(generics.ListAPIView):
    queryset = ZuoZi.objects.all()  # 查询所有ZuoZi对象
    serializer_class = ZuoZiSerializer  # 使用我们定义的序列化器

class ServeImageView(View):
    def get(self, request, tupianpath):
        try:
            file_path = default_storage.path(tupianpath)
            
            with open(file_path,'rb') as f:
                image_data = f.read()
                
            return HttpResponse(image_data,content_type='image/jpeg')
        except FileNotFoundError:
            return HttpResponse(status=404)
