from django.db import models
from django.contrib.auth.models import AbstractUser
from universities.models import University, School


class Subscriber(AbstractUser):
    age = models.IntegerField(blank=True)
    subscription = models.BooleanField(default=False)
    university = models.ForeignKey(University, blank=True, unique=False, null=True, on_delete=models.PROTECT)
    school = models.ForeignKey(School, blank=True, unique=False, null=True, on_delete=models.PROTECT)
