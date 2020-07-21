from django.urls import path
from .views import Courses

urlpatterns = [
    path('', Courses.as_view()),
]
