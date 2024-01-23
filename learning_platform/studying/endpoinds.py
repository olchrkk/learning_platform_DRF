from django.db.models import Subquery
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from mentorship.models import TeacherGroup
from .models import Specification, Course, Topic, ArticleImage, Article
from .serializers import SpecificationSerializer, CourseSerializer, TopicSerializer, ArticleImageSerializer, ArticleSerializer
from mentorship.models import Student
from mentorship.serializers import StudentSerializer, TeacherGroupSerializer
from testing_system.models import Test
from testing_system.serializers import TestSerializer
from rest_framework.response import Response


class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    permission_classes = [permissions.AllowAny]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.AllowAny]


class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
    permission_classes = [permissions.AllowAny]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]


class CourseStudentAPIView(ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        student = self.kwargs["pk"] # получаем ид студента
        student_group = TeacherGroup.objects.filter(student_id__in=student) #находим в группе ид студентов = переданному ид
        course = Course.objects.filter(id__in=student_group.values('course_id')) #фильтруем ид курсов где ид = полю курс ид
        return course


class CourseStudentsAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        course_id = self.kwargs['pk']
        student_group = TeacherGroup.objects.filter(id__in=course_id)
        students_in = Student.objects.filter(id__in=student_group.values('student_id'))
        return students_in


class CourseTopicsAPIView(APIView):
    def get(self, request, pk):
        topics_by_course = Topic.objects.filter(course_id__id=pk)
        serializer = TopicSerializer(topics_by_course, many=True)

        return Response(serializer.data)

    # serializer_class = TopicSerializer
    # permission_classes = [permissions.AllowAny]
    # def get_queryset(self):
    #     course_id = self.kwargs['pk']
    #     topic = Topic.objects.filter(course_id__id=course_id)
    #     return topic


class CourseArticlesAPIView(ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        course_id = self.kwargs['pk']
        articles = Article.objects.filter(topic_id__course_id=course_id)
        return articles


class CourseTestsAPIView(ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        course_id = self.kwargs['pk']
        tests = Test.objects.filter(topic_id__course_id=course_id)
        return tests


class CourseRecommendationAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        student = self.kwargs['pk']
        student_groups = TeacherGroup.objects.filter(student_id=student) #вывели группы в которых содержится студент
        classmates = Student.objects.filter(id__in=Subquery(student_groups.values('student_id')))  #their_courses = Course.objects.filter(id__in=student_groups.values('course_id')) #курсы

        # find his classmates - looking for their courses
        course = Course.objects.filter(id__in=student_groups.values('course_id'))  # фильтруем ид курсов где ид = полю курс ид

        # recommended_courses = their_courses.exclude(id__in=course.values('id'))
        return classmates
