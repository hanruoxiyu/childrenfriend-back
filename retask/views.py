from django.shortcuts import render
# questions/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Retask
from .serializers import RetaskSerializer
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView

class RetaskListCreateView(generics.ListCreateAPIView):
    queryset = Retask.objects.all()
    serializer_class = RetaskSerializer

class RetaskDeleteView(View):
    def delete(self, request, task_id):
        retask = Retask.objects.get(task_id= task_id)
        retask.delete()
        return JsonResponse({"status": "success", "message":f"Question with id {task_id} deleted successfully."},status=204)

class RetaskCreateView(APIView):
    def post(self, request, format=None):
        serializer = RetaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetaskGetByIdView(View):
    def get(self, request, task_id):
        try:
            task = Retask.objects.get(task_id = task_id)
            task_date = {
                    'task_id': task.task_id,
                    'task': task.task,
                    'time': task.time,
                    'circle': task.circle,
                }
            return JsonResponse(task_date)
        except Exam.DoesNotExist:
            return JsonResponse({'error': 'task not found'},status=404)


class RetaskUpdateAPIView(generics.RetrieveAPIView, generics.UpdateAPIView):
    
    queryset = Retask.objects.all()
    serializer_class = RetaskSerializer
    lookup_field = 'task_id'
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
