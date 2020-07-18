from rest_framework import serializers
from .models import *


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('university_name', 'acronym')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'school_name']


class UniversitySchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = UniversitySchool
        fields = ['school']
