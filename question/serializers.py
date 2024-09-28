# questions/serializers.py
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'  # 序列化所有字段