from rest_framework import serializers

from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['course_name']


class ReinforceCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = ['course_name']
