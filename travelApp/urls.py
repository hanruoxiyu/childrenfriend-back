from django.urls import path
from travelApp import views

urlpatterns = [
    path('location', views.RouteAPIView.as_view(), name='weather'),
    ]
