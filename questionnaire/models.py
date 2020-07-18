from django.db import models
from subscription.models import Subscriber


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class Topic(models.Model):
    topic_name = models.CharField(max_length=254)

    def __str__(self):
        return self.topic_name


class Reinforce(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.PROTECT, unique=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, unique=False)


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
