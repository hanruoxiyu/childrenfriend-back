from django.db import models


# Create your models here.
# 趣事
class Diary(models.Model):
    content = models.TextField()
    user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


# 照片
class Photo(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    path2 = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'photo'


# 视频
class Video(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    path2 = models.CharField(max_length=100)
    pic = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'video'


# 成长记录
class Grow_record(models.Model):
    filename = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    path2 = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)

    class Meta:
        db_table = 'grow_record'


class Chat_record(models.Model):
    client = models.CharField(max_length=500)
    robot = models.CharField(max_length=500)
    query_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_record'
