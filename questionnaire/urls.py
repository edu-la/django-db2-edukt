from questionnaire import views
from django.urls import path

urlpatterns = [
    path('', views.PublishQuestionnaire.as_view(), name='questionnaire-list'),
    path('courses/<int:course_id>', views.QuestionnaireByCourse.as_view(), name='questionnaire-by-course'),
    path('course/<int:course_id>/topic/<int:topic_id>', views.QuestionnaireByCourseAndTopic.as_view()),
    path('<int:pk>', views.QuestionnaireDetail.as_view(), name='questionnaire-detail'),
]
