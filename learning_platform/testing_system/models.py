from django.db import models
from mentorship.models import Student, Teacher
from studying.models import Article, Topic
from users.models import DateTimeMixin


class Test(DateTimeMixin, models.Model):
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Test name", unique=True)
    description = models.TextField(verbose_name="Description")
    creator_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    time_limit = models.FloatField(verbose_name="Time limit")

    def __str__(self):
        return f"{self.name} - {self.description}"


class Questions(DateTimeMixin, models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Question", unique=True)

    def __str__(self):
        return f"{self.name}"


class AnswerOption(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50, verbose_name="Answer")
    is_correct = models.BooleanField(verbose_name="True/False")

    def __str__(self):
        return f"{self.answer}"


class CompletedTest(models.Model):
    user_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)


class CompletedArticle(models.Model):
    user_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)


class Attempt(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_at = models.DateTimeField(verbose_name="Start")
    finish_at = models.DateTimeField(verbose_name="Finish")
    points = models.CharField(max_length=100, default="0", verbose_name="points")
