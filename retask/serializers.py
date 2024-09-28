from rest_framework import serializers
from .models import Retask

class RetaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retask
        fields = '__all__'  # 序列化所有字段
