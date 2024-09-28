# questions/urls.py
from django.urls import path
from .views import QuestionListCreateView, QuestionCreateView, QuestionDeleteView, QuestionGetByIdView, QuestionUpdateAPIView

urlpatterns = [
    path('question/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('addquestion/', QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:question_id>/', QuestionDeleteView.as_view(), name='question_delete'),
    path('getquestion/<int:question_id>/',QuestionGetByIdView.as_view(), name='question-get-by-id'),
    path('updatequestion/<int:question_id>/',QuestionUpdateAPIView.as_view(), name='question-update'),
]
