from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from itertools import chain

from studying.models import Course
from .models import Student, Teacher, TeacherGroup
from .serializers import StudentSerializer, TeacherSerializer, TeacherGroupSerializer, FiltersSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]


class TeacherGroupViewSet(viewsets.ModelViewSet):
    queryset = TeacherGroup.objects.all()
    serializer_class = TeacherGroupSerializer
    permission_classes = [permissions.AllowAny]


class SpecificationTeacherAPIView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        specification_id = self.kwargs['pk']
        teacher = Teacher.objects.filter(specification_id__id=specification_id)
        return teacher


class StudentsAndTeachersAPIView(ListAPIView):
    serializer_class = FiltersSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        teachers = Teacher.objects.all()
        students = Student.objects.all()
        queryset = chain(teachers, students)
        return queryset
