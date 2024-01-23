from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Specification, Course, Topic, Article, ArticleImage


class SpecificationSerializer(ModelSerializer):
    class Meta:
        model = Specification
        fields = ["id", "name"]


class CourseSerializer(ModelSerializer):
    creater_id = serializers.ReadOnlyField(source="creater_id.id")
    specification_id = SpecificationSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "creater_id", "specification_id"]


class TopicSerializer(ModelSerializer):
    course_id = serializers.ReadOnlyField(source="course_id.id")

    class Meta:
        model = Topic
        fields = ["id", "name", "description", "course_id"]


class ArticleImageSerializer(ModelSerializer):
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = ArticleImage
        fields = ["id", "image_url"]


class ArticleSerializer(ModelSerializer):
    topic_id = serializers.ReadOnlyField(source="topic_id.id")
    creator_id = serializers.ReadOnlyField(source="creator_id.id")
    article_image_id = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ["id", "topic_id", "creator_id", "name", "content", "is_completed", "article_image_id"]
