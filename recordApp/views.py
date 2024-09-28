from datetime import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from recordApp.models import Diary, Photo, Video, Grow_record, Chat_record
from recordApp.serializers import DiarySerializer, PhotoSerializer, VideoSerializer, GrowSerializer, ChatSerializer,HeightSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Diary
from .serializers import DiarySerializer

class DiaryList(APIView):
    """
    列出所有日记或创建新日记
    """
    def get(self, request, format=None):
        user = request.user
        diary = Diary.objects.filter(user=user.id).order_by('-created_at').all()
        serializer = DiarySerializer(diary, many=True)  # 序列化
        return Response(serializer.data)
    # 创建趣事
    def post(self, request, format=None):
        request.data['user'] = request.user.id
        request.data['created_at'] = datetime.now()
        serializer = DiarySerializer(data=request.data)   # 反序列化
        # serializer检验
        if serializer.is_valid():
            serializer.save()  # 将符合条件的数据插入到数据库
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 删除趣事
class DiaryDetail(APIView):
    """
    检索、更新或删除一个日记实例
    """
    def get_object(self, pk):
        return Diary.objects.get(pk=pk)
    def get(self, request, pk, format=None):
        diary = self.get_object(pk)
        diary.delete()
        return Response(status=status.HTTP_200_OK)



class PhotoList(APIView):
    def get(self, request):
        photos = Photo.objects.order_by("-create_date").all()
        serializer = PhotoSerializer(photos, many=True)  # 序列化
        scheme = request.scheme
        host = request.get_host()
        server_url = scheme + '://' + host
        return Response({"host":server_url,"details":serializer.data})
class PhotoDel(APIView):
    def get(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# 查询视频列表，核心就是数据库查询，然后进行序列化，
class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.order_by("-create_date").all()
        serializer = VideoSerializer(videos, many=True)     # 序列化
        scheme = request.scheme
        host = request.get_host()
        server_url =    scheme + '://' + host

        return Response({"host":server_url,"details":serializer.data})
# 删除视频，前端传入id，然后删除
class VideoDel(APIView):
    def get(self, request, pk):
        video = Video.objects.get(pk=pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 查询成长记录列表
class Grow_recordList(APIView):
    def get(self, request):
        grow_record = Grow_record.objects.order_by("-create_date").all()
        serializer = GrowSerializer(grow_record, many=True)  # 序列化
        scheme = request.scheme
        host = request.get_host()
        server_url = scheme + '://' + host
        return Response({"host":server_url,"details":serializer.data})
# 删除成长记录
class Grow_recodDel(APIView):
    def get(self, request, pk):
        grow_data = Grow_record.objects.get(pk=pk)
        grow_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 系统服务记录列表
class ServerList(APIView):
    def get(self, request):
        server_records = Chat_record.objects.order_by("query_time").all()
        serializer = ChatSerializer(server_records, many=True)  # 序列化
        scheme = request.scheme
        host = request.get_host()
        server_url = scheme + '://' + host
        return Response({"host":server_url,"details":serializer.data})

class Height_recordList(APIView):
    def get(self, request):
        height_records = Grow_record.objects.values("height", "weight", "create_date").order_by("-create_date").all()[:10]
        serializer = HeightSerializer(height_records, many=True)  # 序列化
        scheme = request.scheme
        host = request.get_host()
        server_url = scheme + '://' + host
        return Response({"host":server_url,"details":serializer.data})