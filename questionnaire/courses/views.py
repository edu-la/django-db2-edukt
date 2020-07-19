from rest_framework import generics

from . import models
from . import serializers


class CoursesBySubscriberId(generics.ListAPIView):
    serializer_class = serializers.ReinforceCourseSerializer

    def get_queryset(self):
        return models.Course.objects.filter(reinforce__subscriber_id=self.kwargs['subscriber_id'])
