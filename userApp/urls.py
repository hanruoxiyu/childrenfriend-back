from django.urls import path
from userApp import views
from .views import LoginView,RegisterView
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    ]
