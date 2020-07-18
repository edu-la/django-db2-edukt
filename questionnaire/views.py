from rest_framework import generics

from questionnaire.models import Questionnaire, Question
from questionnaire.serializers import QuestionnaireSerializer, QuestionSerializer


class PublishQuestionnaire(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class QuestionnaireDetails(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        response = []

        for question in Question.objects.filter(questionnaire_id=self.kwargs['questionnaire_id']):
            body = {
                "description": question.description,
                "alternatives": question.alternative_set.all()
            }
            response.append(body)

        return response
