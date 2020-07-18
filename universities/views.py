from rest_framework import generics

from .serializers import *


class UniversityList(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    # permission_classes =


class SchoolListById(generics.ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):

        q = School.objects.filter(universityschool__university=self.kwargs['university_id'])
        return q


class SchoolListByAcronym(generics.ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        q = School.objects.filter(universityschool__university__acronym=self.kwargs['acronym'])
        return q
