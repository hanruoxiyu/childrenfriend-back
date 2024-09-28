from django.urls import path
from .views import ZuoZiListAPIView, ServeImageView

urlpatterns = [
    path('zuozi/', ZuoZiListAPIView.as_view(), name='zuozi_list'),
    path('images/<path:tupianpath>/', ServeImageView.as_view(), name='serve_image'),
]
