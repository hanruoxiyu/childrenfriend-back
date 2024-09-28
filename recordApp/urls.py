from django.urls import path, include
from rest_framework import routers

from userApp import views
from .views import DiaryList, DiaryDetail, PhotoList, PhotoDel, VideoList, VideoDel, Grow_recordList, Grow_recodDel, \
    ServerList, Height_recordList

# 路由列表
urlpatterns = [
    path('diaries/', DiaryList.as_view(), name='diary-list'),
    path('diariesdel/<int:pk>', DiaryDetail.as_view(), name='diary-del'),

    path('photos/', PhotoList.as_view(), name='photos-list'),
    path('photodel/<int:pk>', PhotoDel.as_view(), name='photodel-del'),
    path('video/', VideoList.as_view(), name='video-list'),
    path('videodel/<int:pk>', VideoDel.as_view(), name='video-del'),
    path('grow/', Grow_recordList.as_view(), name='grow-list'),
    path('growdel/<int:pk>', Grow_recodDel.as_view(), name='grow-del'),
    path('serverlist/', ServerList.as_view(), name='server-list'),
    path('growdata/', Height_recordList.as_view(), name='grow_data-list'),

]
