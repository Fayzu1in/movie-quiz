from .models import Question
from .serializers import QuestionSerializer
from django.http import JsonResponse
from rest_framework import generics 


def question_list(request):
    #? API GET 
    if request.method == 'GET':
        questiions = Question.objects.all()
        serializer = QuestionSerializer(questiions, many=True)
        return JsonResponse(serializer.data, safe=False)


    #? API POST 
    elif request.method == "POST": 
        question = request.POST 
        serializer = QuestionSerializer(data=question)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)


class QuestionListApiView(generics.ListAPIView): 
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailApiView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionUpdateApiView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
