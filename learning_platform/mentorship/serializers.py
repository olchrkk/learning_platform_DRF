from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Student, Teacher, TeacherGroup


class StudentSerializer(ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user_id.id")

    class Meta:
        model = Student
        fields = ["id", "user_id", "rating"]


class TeacherSerializer(ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user_id.id")
    specification_id = serializers.ReadOnlyField(source="specification_id.id")

    class Meta:
        model = Teacher
        fields = ["id", "user_id", "specification_id"]


class TeacherGroupSerializer(ModelSerializer):
    teacher_id = serializers.ReadOnlyField(source="teacher_id.id")
    course_id = serializers.ReadOnlyField(source="course_id.id")
    student_id = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = TeacherGroup
        fields = ["id", "teacher_id", "course_id", "student_id", "name"]


class FiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSerializer
        fields = '__all__'

    def to_representation(self, object):
        if isinstance(object, Student):
            serializer = StudentSerializer(object)
        elif isinstance(object, Teacher):
            serializer = TeacherSerializer(object)
        else:
            raise ValueError
        return serializer.data
