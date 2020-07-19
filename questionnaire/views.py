from rest_framework import generics

from questionnaire.models import Questionnaire, Question
from questionnaire import serializers


class PublishQuestionnaire(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = serializers.QuestionnaireSerializer


class QuestionnaireDetail(generics.ListAPIView):
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        response = []

        for question in Question.objects.filter(questionnaire_id=self.kwargs['pk']):
            body = {
                "description": question.description,
                "alternatives": question.alternative_set.all()
            }
            response.append(body)

        return response


class QuestionnaireByCourse(generics.ListAPIView):
    serializer_class = serializers.QuestionnaireHyperlinkedSerializer

    def get_queryset(self):
        return Questionnaire.objects.filter(course_id=self.kwargs['course_id'])


class QuestionnaireByCourseAndTopic(generics.ListAPIView):
    serializer_class = serializers.QuestionnaireHyperlinkedSerializer

    def get_queryset(self):
        return Questionnaire.objects.filter(course_id=self.kwargs['course_id'], topic_id=self.kwargs['topic_id'])
