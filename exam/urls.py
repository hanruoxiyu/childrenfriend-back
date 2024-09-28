from django.urls import path
from .views import ExamListView, ExamGetByIdView

urlpatterns = [
    path('exam/', ExamListView.as_view(), name='exam_list'),
    path('exam/<int:score_id>/',ExamGetByIdView.as_view(), name='exam-get-by-id'),
]
