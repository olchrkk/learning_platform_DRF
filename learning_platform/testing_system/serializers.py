from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Test, Questions, AnswerOption, CompletedTest, CompletedArticle, Attempt


class TestSerializer(ModelSerializer):
    topic_id = serializers.ReadOnlyField(source="topic_id.id")
    creator_id = serializers.ReadOnlyField(source="creator_id.id")

    class Meta:
        model = Test
        fields = ["id", "topic_id", "name", "description", "creator_id", "time_limit"]


class QuestionsSerializer(ModelSerializer):
    test_id = serializers.ReadOnlyField(source="test_id.id")

    class Meta:
        model = Questions
        fields = ["id", "test_id", "name"]


class AnswerOptionSerializer(ModelSerializer):
    question_id = serializers.ReadOnlyField(source="question_id.id")

    class Meta:
        model = AnswerOption
        fields = ["id", "question_id", "answer", "is_correct"]


class CompletedTestSerializer(ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user_id.id")
    test_id = serializers.ReadOnlyField(source="test_id.id")

    class Meta:
        model = CompletedTest
        fields = ["id", "user_id", "test_id"]


class CompletedArticleSerializer(ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user_id.id")
    article_id = serializers.ReadOnlyField(source="article_id.id")

    class Meta:
        model = CompletedArticle
        fields = ["id", "user_id", "article_id"]


class AttemptSerializer(ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user_id.id")
    test_id = serializers.ReadOnlyField(source="test_id.id")

    class Meta:
        model = Attempt
        fields = ["id", "test_id", "user_id", "start_at", "finish_at", "points"]
