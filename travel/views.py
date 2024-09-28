from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Travel
from .serializers import TravelSerializer

class TravelListCreateView(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def perform_create(self, serializer):
        # 如果需要在创建时额外处理数据，可以在这里做
        serializer.save()
# Create your views here.
