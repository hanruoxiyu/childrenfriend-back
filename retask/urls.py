from django.urls import path, include
from .views import RetaskListCreateView, RetaskDeleteView, RetaskGetByIdView, RetaskUpdateAPIView, RetaskCreateView


urlpatterns = [
    path('retask/', RetaskListCreateView.as_view(), name='get-task'),
    path('deletetask/<int:task_id>/', RetaskDeleteView.as_view(), name='delete_task'),
    path('gettask/<int:task_id>/',RetaskGetByIdView.as_view(), name='task-get-by-id'),
    path('updatetask/<int:task_id>/',RetaskUpdateAPIView.as_view(), name='task-update'),
    path('addtask/', RetaskCreateView.as_view(), name='task_create'),
]
