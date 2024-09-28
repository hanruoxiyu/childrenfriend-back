from django.urls import path
from .views import ReminderListCreateView

urlpatterns = [
    path('reminder/', ReminderListCreateView.as_view(), name='reminder_list_create'),
]