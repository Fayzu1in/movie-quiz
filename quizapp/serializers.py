from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.Serializer):
    questionImage = serializers.ImageField()
    answer1 = serializers.CharField(max_length=100)
    answer2 = serializers.CharField(max_length=100)
    answer3 = serializers.CharField(max_length=100)
    answer4 = serializers.CharField(max_length=100)
    answers = serializers.CharField(max_length=30)

    def create(self, validated_data):
        questionImage = validated_data.get('questionImage')
        answer1 = validated_data.get('answer1')
        answer2 = validated_data.get('answer2')
        answer3 = validated_data.get('answer3')
        answer4 = validated_data.get('answer4')
        answers = validated_data.get('an')
        return Question.objects.create(
            questionImage=questionImage, answer1=answer1,
            answer2=answer2, answer3=answer3, answer4=answer4, correct=answers
        )

    def update(self, instance, validated_data):
        questionImage = validated_data.get(
            'questionImage', instance.questionImage)
        instance.questionImage = questionImage
        answer1 = validated_data.get('answer1', instance.question1)
        instance.answer1 = answer1
        answer2 = validated_data.get('answer2', instance.question2)
        instance.answer1 = answer2
        answer3 = validated_data.get('answer3', instance.question3)
        instance.answer1 = answer3
        answer4 = validated_data.get('answer4', instance.question4)
        instance.answer1 = answer4
        answers = validated_data.get('answers', instance.answers)
        instance.correct = answers
        instance.save()
        return instance
