from django.db import models
from users.models import DateTimeMixin


class Specification(models.Model):
    name = models.CharField(max_length=50, verbose_name="Specification")

    def __str__(self):
        return f"{self.name}"


class Course(DateTimeMixin, models.Model):
    name = models.CharField(max_length=50, verbose_name="Course")
    creater_id = models.ForeignKey("mentorship.Teacher", on_delete=models.CASCADE)
    specification_id = models.ManyToManyField(Specification)

    def __str__(self):
        return f"{self.name}"

    def specification(self):
        return ",".join([str(p) for p in self.specification_id.all()])


class Topic(DateTimeMixin, models.Model):
    name = models.CharField(max_length=50, verbose_name="Topic name", unique=True)
    description = models.TextField(verbose_name="Description")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class ArticleImage(models.Model):
    image = models.ImageField(upload_to="source/", blank=False)


class Article(DateTimeMixin, models.Model):
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    creator_id = models.ForeignKey(
        "mentorship.Teacher", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=50, verbose_name="Topic name", unique=True)
    content = models.TextField(verbose_name="Content")
    is_completed = models.BooleanField(verbose_name="True/False")
    article_image_id = models.ManyToManyField(ArticleImage)

    def __str__(self):
        return f"{self.name}"

    def get_article_image_id(self):
        return ",".join([str(p) for p in self.article_image_id.all()])
