# questions/serializers.py
from rest_framework import serializers
from .models import Travel  # 确保导入正确的模型


class TravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travel
        fields = '__all__'  # 或者具体列出需要的字段
