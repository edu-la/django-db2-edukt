from knox import views as knox_views

from questionnaire.courses.views import CoursesBySubscriberId
from .views import RegisterAPI, LoginAPI
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('<int:subscriber_id>/courses', CoursesBySubscriberId.as_view(), name='courses-subscriber')
]
