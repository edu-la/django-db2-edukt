from .views import *
from django.urls import path

urlpatterns = [
    path('', PublishQuestionnaire.as_view()),
    path('<int:questionnaire_id>', QuestionnaireDetails.as_view())
]

