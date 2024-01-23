from django.db import models
from studying.models import Specification
from users.models import CustomUser


class Student(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100, default="0", verbose_name="rating")

    def __str__(self):
        return f"{self.id}"


class Teacher(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    specification_id = models.ForeignKey(
        Specification, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.user_id}"


class TeacherGroup(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    course_id = models.ForeignKey("studying.Course", on_delete=models.CASCADE)
    student_id = models.ManyToManyField(Student)
    name = models.CharField(max_length=50, verbose_name="Teacher group")

    def __str__(self):
        return f"{self.teacher_id}"
