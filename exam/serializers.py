from rest_framework import serializers
from .models import Exam

class ExamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exam
        fields = '__all__'  # 包括所有字段，也可以指定具体字段列表
