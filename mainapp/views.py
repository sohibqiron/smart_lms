from django.shortcuts import render
from django.contrib.auth.models import User, Group 
from rest_framework import generics,viewsets,permissions
from .models import *
from .serializers import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BaseGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BaseGroup.objects.all()
    serializer_class = BaseGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Api for mentor

class MentorList(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    

class MentorCreate(generics.CreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

#-------------------------

#Api for group


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupCreate(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#--------------------

#Api for student

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer