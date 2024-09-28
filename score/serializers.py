# questions/serializers.py
from rest_framework import serializers
from .models import Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'  # 序列化所有字段