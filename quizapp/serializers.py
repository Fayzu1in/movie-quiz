from rest_framework import serializers
from .models import Question, Qst


class QuestionSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    questionImage = serializers.ImageField()
    answer1 = serializers.CharField(max_length=100)
    answer2 = serializers.CharField(max_length=100)
    answer3 = serializers.CharField(max_length=100)
    answer4 = serializers.CharField(max_length=100)
    correct = serializers.CharField(max_length=30)

    def create(self, validated_data):
        questionImage = validated_data.get('questionImage')
        answer1 = validated_data.get('answer1')
        answer2 = validated_data.get('answer2')
        answer3 = validated_data.get('answer3')
        answer4 = validated_data.get('answer4')
        correct = validated_data.get('correct')
        return Question.objects.create(
            questionImage=questionImage, answer1=answer1,
            answer2=answer2, answer3=answer3, answer4=answer4, correct=correct
        )

    def update(self, instance, validated_data):
        questionImage = validated_data.get(
            'questionImage', instance.questionImage)
        instance.questionImage = questionImage
        answer1 = validated_data.get('answer1', instance.answer1)
        instance.answer1 = answer1
        answer2 = validated_data.get('answer2', instance.answer2)
        instance.answer1 = answer2
        answer3 = validated_data.get('answer3', instance.answer3)
        instance.answer1 = answer3
        answer4 = validated_data.get('answer4', instance.answer4)
        instance.answer1 = answer4
        correct = validated_data.get('correct', instance.correct)
        instance.correct = correct
        instance.save()
        return instance


class QstSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    questionImage = serializers.ImageField()
    answerText = serializers.CharField(max_length=100)
    isCorrect = serializers.BooleanField()

    def create(self, validated_data):
        questionImage = validated_data.get('questionImage')
        answerText = validated_data.get('answerText')
        isCorrect = validated_data.get('isCorrect')
        return Qst.objects.create(questionImage=questionImage, answerText=answerText, isCorrect=isCorrect)

    def update(self, instance, validated_data):
        questionImage = validated_data.get(
            'questionImage', instance.questionImage)
        instance.questionImage = questionImage
        answerText = validated_data.get('answerText', instance.answerText)
        instance.answerText = answerText
        isCorrect = validated_data.get('isCorrect', instance.isCorrect)
        instance.isCorrect = isCorrect
