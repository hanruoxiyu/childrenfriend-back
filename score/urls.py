from django.urls import path
from .views import ScoreListView

urlpatterns = [
    path('score/', ScoreListView.as_view(), name='score_list'),
]