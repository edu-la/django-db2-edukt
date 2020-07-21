from django.db import models
from django.contrib.auth.models import AbstractUser
from questionnaire.models import Questionnaire
from questionnaire.courses.models import Course
from universities.models import University, School


class Subscriber(AbstractUser):
    age = models.IntegerField(blank=True)
    subscription = models.BooleanField(default=False)
    university = models.ForeignKey(University, blank=True, unique=False, null=True, on_delete=models.PROTECT)
    school = models.ForeignKey(School, blank=True, unique=False, null=True, on_delete=models.PROTECT)


class QuestionnaireMeta(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.PROTECT, unique=False)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT, unique=False)
    favourite = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=7, decimal_places=3)
    good = models.IntegerField()
    bad = models.IntegerField()
    no_ans = models.IntegerField()
    date_done = models.DateField()


class Reinforce(models.Model):
    subscriber = models.ForeignKey('Subscriber', on_delete=models.PROTECT, unique=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, unique=False)
