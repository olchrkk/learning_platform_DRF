from django.contrib import admin
from django.db.models import Count

from .models import Student, Teacher, TeacherGroup

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'rating']
    list_filter = ['rating']
    ordering = ('-id',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id']

@admin.register(TeacherGroup)
class TeacherGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_id', 'course_id', 'name', 'student_count']
    list_display_links = ('id', 'name')

    def student_count(self, obj):
        return obj.student_count
    student_count.short_description = 'Students'

    def get_queryset(self, request):
        queryset = TeacherGroup.objects.annotate(
            student_count=Count('student_id__id')
        )
        return queryset


