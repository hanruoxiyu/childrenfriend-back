# questions/serializers.py
from rest_framework import serializers
from .models import ZuoZi

class ZuoZiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZuoZi
        fields = '__all__'  # 这意味着我们将序列化模型的所有字段