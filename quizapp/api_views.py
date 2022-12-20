from .models import Question
from .serializers import QuestionSerializer
from django.http import JsonResponse


def question_list(request):
    if request.method == 'GET':
        questiions = Question.objects.all()
        serializer = QuestionSerializer(questiions, many=True)
        return JsonResponse(serializer.data, safe=False)
