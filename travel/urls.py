from django.urls import path
from .views import TravelListCreateView

urlpatterns = [
    path('travel/', TravelListCreateView.as_view(), name='Travel_list_create'),
]
