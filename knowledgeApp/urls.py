from django.urls import path
from knowledgeApp.views import QAListView

urlpatterns = [
    path('qa/', QAListView.as_view(), name='qa_list'),
]
