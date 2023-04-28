from django.urls import path 
from .views import *

urlpatterns = [
    path('mentor-list/',MentorList.as_view()),
    path('mentor-create/',MentorCreate.as_view()),

    path('group-list/',GroupList.as_view()),
    path('group-create/',GroupCreate.as_view()),

    path('student-list/',StudentList.as_view()),
    path('student-create/',StudentCreate.as_view()),
]
