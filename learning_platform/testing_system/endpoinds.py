from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView

from .models import Test, Questions, AnswerOption, CompletedTest, CompletedArticle, Attempt
from .serializers import TestSerializer, QuestionsSerializer, AnswerOptionSerializer, CompletedTestSerializer, CompletedArticleSerializer, AttemptSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.AllowAny]


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.AllowAny]


class AnswerOptionViewSet(viewsets.ModelViewSet):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionSerializer
    permission_classes = [permissions.AllowAny]


class CompletedTestViewSet(viewsets.ModelViewSet):
    queryset = CompletedTest.objects.all()
    serializer_class = CompletedTestSerializer
    permission_classes = [permissions.AllowAny]


class CompletedArticleViewSet(viewsets.ModelViewSet):
    queryset = CompletedArticle.objects.all()
    serializer_class = CompletedArticleSerializer
    permission_classes = [permissions.AllowAny]


class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
    permission_classes = [permissions.AllowAny]

class TestQuestionsAPIView(ListAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        test_id = self.kwargs['id']
        questions = Questions.objects.filter(test_id__id=test_id)
        return questions

class QuestionAnswerAPIView(ListAPIView):
    serializer_class = AnswerOptionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        question_id = self.kwargs['id']
        answer = AnswerOption.objects.filter(question_id__id=question_id)
        return answer
