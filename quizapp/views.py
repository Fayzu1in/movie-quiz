from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from .models import Question
# from .forms import QuestionForm
import json

questions = Question.objects.all()
data = []


class HomeView(TemplateView):
    global data
    template_name = "test.html"
    data = []
    questionData = {}
    print(questions[0].answer1)
    for question in questions:
        questionData = {
            'questionImage': question.questionImage.url,
            'answerText1': question.answer1,
            'answerText2': question.answer2,
            'answerText3': question.answer3,
            'answerText4': question.answer4,
            'correctAnswer': question.answers
        }
        data.append(questionData)

    def get_context_data(self, **kwargs):
        global data
        context = super().get_context_data(**kwargs)
        context["questions"] = questions
        context['data'] = json.dumps(data)
        return context
