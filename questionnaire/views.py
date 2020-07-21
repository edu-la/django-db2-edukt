from django.db import connection
from django.db.utils import OperationalError
from rest_framework import generics, status
from rest_framework.response import Response

from questionnaire.models import Questionnaire, Question, Alternative
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


class SolveQuestionnaire(generics.ListCreateAPIView):
    serializer_class = serializers.SolveQuestionnaireSerializer

    def post(self, request, *args, **kwargs):

        correct = 0
        incorrect = 0
        for answer in self.request.data['answers']:
            if Alternative.objects.get(id=answer).correct_alt:
                correct += 1
            else:
                incorrect += 1

        with connection.cursor() as cursor:
            try:
                cursor.callproc('registerTestQResult',
                                [self.kwargs['subscriber_username'], self.kwargs['pk'], correct, incorrect])

                return Response({
                    "correct": correct,
                    "incorrect": incorrect
                }, status=status.HTTP_201_CREATED)

            except OperationalError as db:
                serializer = serializers.HandleError({
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": db
                })

                return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
