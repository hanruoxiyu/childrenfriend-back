from django.shortcuts import render
from rest_framework import generics
from .models import Exam
from .serializers import ExamSerializer
from django.views import View
from django.http import JsonResponse

class ExamListView(generics.ListAPIView):
    queryset = Exam.objects.all()  # 查询所有Exam记录
    serializer_class = ExamSerializer  # 使用上面定义的序列化器

class ExamGetByIdView(View):
    def get(self, request,score_id):
        try:
            exams = Exam.objects.filter(score_id = score_id)
            
            exam_date = [
                {
                    'question_text': exam.question_text,
                    'useranswer': exam.useranswer,
                    'answer': exam.answer,
                    'iscorrect': exam.iscorrect,
                }
                for exam in exams
            ]
            
            return JsonResponse(exam_date, safe=False)
        except Exam.DoesNotExist:
            return JsonResponse({'error': 'Exam not found'},status=404)
