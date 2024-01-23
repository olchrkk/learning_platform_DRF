from rest_framework import routers
from django.urls import path, include, re_path

from testing_system.endpoinds import TestViewSet, QuestionsViewSet, AnswerOptionViewSet, CompletedTestViewSet,\
    CompletedArticleViewSet, AttemptViewSet, TestQuestionsAPIView, QuestionAnswerAPIView

router = routers.SimpleRouter()

router.register(r'test', TestViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'answeroption', AnswerOptionViewSet)
router.register(r'completedtest', CompletedTestViewSet)
router.register(r'completedarticle', CompletedArticleViewSet)
router.register(r'attempt', AttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path('test/(?P<pk>[^/.]+)/questions', TestQuestionsAPIView.as_view(), name='test-questions'),
    re_path('question/(?P<pk>[^/.]+)/answer', TestQuestionsAPIView.as_view(), name='questions-answer')
]
