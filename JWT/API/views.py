from django.shortcuts import render

# Create your views here.
from .models import Student,Teacher
from .serializers import StudentSerializer,TeacherSerializer
from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
from API.customauth import CustomAuth
from rest_framework.permissions import IsAuthenticated

# for JWT 
from rest_framework_simplejwt.authentication import JWTAuthentication

# how to apply Authentication on class base views
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]





# ReadOnlyModelViewSet give us access to list and retrive methods means we can only read data
# we can not put update patch and delete data

class TeacherModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    

