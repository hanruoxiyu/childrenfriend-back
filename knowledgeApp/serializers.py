from rest_framework import serializers
from knowledgeApp.models import QA

class QASerializer(serializers.ModelSerializer):
    class Meta:
        model = QA
        fields = '__all__'  # 包含所有字段，或者指定具体字段如 ['QA_id', 'child', 'question', 'answer', 'ask_time']
