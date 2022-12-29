from django.urls import path, include, re_path
from .views import *
from . import views, api_views


urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    re_path('', api_views.QuestionListApiView.as_view()),

]
