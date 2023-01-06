from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from quizapp import views, api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/questions/', api_views.question_list),
    path('api/questions/', api_views.QuestionListApiView.as_view()),
    path('api/questions/detail/<int:pk>',
         api_views.QuestionDetailApiView.as_view()),
    path('api/questions/update/<int:pk>',
         api_views.QuestionUpdateApiView.as_view()),
    path('', include('quizapp.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
