from django.db import models
from django.urls import reverse

# Create your models here.


class Question(models.Model):

    options = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4)
    ]

    questionImage = models.ImageField(
        ("Image"), upload_to='quiz_images', height_field=None, width_field=None, max_length=None, null=False)
    answer1 = models.CharField(("Answer 1"), max_length=100, blank=False)
    answer2 = models.CharField(("Answer 2"), max_length=100, blank=False)
    answer3 = models.CharField(("Answer 3"), max_length=100, blank=False)
    answer4 = models.CharField(("Answer 4"), max_length=100, blank=False)
    correct = models.CharField(
        verbose_name='Correct answer is',
        max_length=30,
        choices=options,
        default=False,
    )

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")

    def __str__(self):
        return f'Вопрос: {self.id}'

    def get_absolute_url(self):
        return reverse("Question_detail", kwargs={"pk": self.pk})


class Qst(models.Model):

    questionImage = models.ImageField(("Question picture"), upload_to='quiz_images',
                                      height_field=None, width_field=None, max_length=None, blank=True, null=True)
    answerText = models.CharField(("Question text"), max_length=100)
    isCorrect = models.BooleanField(("Correct"))

    class Meta:
        verbose_name = ("Qst")
        verbose_name_plural = ("Qsts")

    def __str__(self):
        return self.answerText

    def get_absolute_url(self):
        return reverse("Qst_detail", kwargs={"pk": self.pk})
