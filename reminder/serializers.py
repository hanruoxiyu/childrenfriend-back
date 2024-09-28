# questions/serializers.py
from rest_framework import serializers
from .models import Reminder  # 确保导入正确的模型


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = '__all__'  # 或者具体列出需要的字段