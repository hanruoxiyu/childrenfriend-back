from django.shortcuts import render
# questions/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView

class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class QuestionCreateView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(View):
    
    def delete(self, request, question_id):
        question = Question.objects.get(question_id= question_id)
        question.delete()
        return JsonResponse({"status": "success", "message":f"Question with id {question_id} deleted successfully."},status=204)
# Create your views here.
class QuestionGetByIdView(View):
    def get(self, request, question_id):
        try:
            question = Question.objects.get(question_id = question_id)
            question_date = {
                    'question_id': question.question_id,
                    'subject': question.subject,
                    'question_text': question.question_text,
                    'answer': question.answer,
                }
            return JsonResponse(question_date)
        except Exam.DoesNotExist:
            return JsonResponse({'error': 'Question not found'},status=404)


class QuestionUpdateAPIView(APIView):
    
    def put(self, request,question_id):
        try:
            question_instance = Question.objects.get(question_id=question_id)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = QuestionSerializer(question_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
