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
