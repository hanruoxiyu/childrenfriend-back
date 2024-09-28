from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def perform_create(self, serializer):
        # 如果需要在创建时额外处理数据，可以在这里做
        serializer.save()
# Create your views here.
