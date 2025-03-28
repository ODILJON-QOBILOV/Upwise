from django.db import models
from apps.teachers.models import BaseModel
# Create your models here.

class QuizDirection(BaseModel):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Test(BaseModel):
    class Degree(models.TextChoices):
        EASY = 'easy'
        MEDIUM = 'medium'
        HARD = 'hard'

    name = models.CharField(max_length=55)
    degree = models.CharField(max_length=55, choices=Degree.choices, default=Degree.MEDIUM)
    quiz_direction = models.ForeignKey(QuizDirection, on_delete=models.CASCADE, related_name="tests")

    def __str__(self):
        return self.name

class Question(BaseModel):
    question = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.question

class Option(BaseModel):
    option = models.BooleanField(default=False)
    text = models.CharField(max_length=55)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")

    def __str__(self):
        return self.option
