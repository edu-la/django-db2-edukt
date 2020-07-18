from .views import *
from django.urls import path

urlpatterns = [
    path('', UniversityList.as_view(), name='university-list'),
    path('schools/<int:university_id>', SchoolListById.as_view(), name='university-id-school'),
    path('schools/<str:acronym>', SchoolListByAcronym.as_view(), name='university-initials-school')
]
