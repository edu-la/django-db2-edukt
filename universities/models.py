from django.db import models


class University(models.Model):
    university_name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ['university_name']

    def __str__(self):
        return self.university_name + ", " + self.acronym


class School(models.Model):
    school_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['school_name']

    def __str__(self):
        return self.school_name


class UniversitySchool(models.Model):
    university = models.ForeignKey(University, on_delete=models.PROTECT, unique=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT, unique=False)

    def __str__(self):
        return "%s, %s".format()
