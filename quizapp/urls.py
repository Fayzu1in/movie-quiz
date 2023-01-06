from django.urls import path, include, re_path
from . import views, api_views
from .views import *


urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', api_views.QuestionListApiView.as_view()),
    re_path('answers-list', api_views.QstListApiView.as_view()),

]
