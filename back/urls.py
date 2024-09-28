"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userApp import urls as user_url
from knowledgeApp import urls as knowledge_url
from recordApp import urls as record_url
from travelApp import urls as travel_url
from userApp import urls as user_url
from question import urls as question_url
from reminder import urls as reminder_urls
from score import urls as score_urls
from zuozi import urls as zuozi_urls
from retask import urls as retask_urls
from exam import urls as exam_urls
from travel import urls as travel_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('user/',include(user_url)),
    path('knowledge/',include(knowledge_url)),
    path('record/',include(record_url)),
    path('travel/',include(travel_url)),
    path('question/',include(question_url)),
    path('reminder/', include(reminder_urls)),
    path('score/', include(score_urls)),
    path('zuozi/', include(zuozi_urls)),
    path('retask/', include(retask_urls)),
    path('exam/', include(exam_urls)),
    path('travel/', include(travel_url)),
]
