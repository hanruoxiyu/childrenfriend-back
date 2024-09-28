from rest_framework import serializers
from recordApp.models import Diary, Photo, Video, Grow_record, Chat_record


# 创建序列化器类，在视图中调用
# 趣事序列化
class DiarySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Diary
        # 对表中哪些字段做序列化
        fields = ['id', 'user', 'content', 'created_at']
        extra_kwargs = {
            'id': {'required': False}
        }
# 照片序列化
class PhotoSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Photo
        fields = ('id', 'name', 'path2', 'create_date')
# 视频序列化

class VideoSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Video
        fields = ('id', 'name', 'path2', 'pic','create_date')

# 成长记录序列化
class GrowSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Grow_record
        fields = ('id', 'filename', 'path2', 'create_date','height','weight')

# 服务记录序列化
class ChatSerializer(serializers.ModelSerializer):
    query_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Chat_record
        fields = ('id', 'client', 'robot', 'query_time')
        
# 成长记录序列化
class HeightSerializer(serializers.ModelSerializer):
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Grow_record
        fields = ('id', 'create_date', 'height', 'weight')