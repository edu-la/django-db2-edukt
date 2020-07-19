from django.db import models

from questionnaire.courses.models import Course, Topic


class Questionnaire(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, unique=False)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, unique=False)


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT, unique=False)
    description = models.CharField(max_length=500)


class Alternative(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, unique=False)
    description = models.CharField(max_length=500)
    correct_alt = models.BooleanField(default=False)
