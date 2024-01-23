from rest_framework import routers
from django.urls import path, include, re_path

from studying.endpoinds import SpecificationViewSet, CourseViewSet, TopicViewSet, ArticleImageViewSet, ArticleViewSet,\
    CourseStudentAPIView, CourseStudentsAPIView, CourseTopicsAPIView, CourseArticlesAPIView, CourseTestsAPIView,\
    CourseRecommendationAPIView

router = routers.SimpleRouter()

router.register(r'specification', SpecificationViewSet)
router.register(r'course', CourseViewSet)
router.register(r'topic', TopicViewSet)
router.register(r'articleimage', ArticleImageViewSet)
router.register(r'article', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path('student/(?P<pk>[^/.]+)/course/', CourseStudentAPIView.as_view(), name='course-student'),
    re_path('course/(?P<pk>[^/.]+)/students', CourseStudentsAPIView.as_view(), name='course-students'),
    re_path('course/(?P<pk>[^/.]+)/topics', CourseTopicsAPIView.as_view(), name='course-topics'),
    re_path('course/(?P<pk>[^/.]+)/articles', CourseArticlesAPIView.as_view(), name='course-articles'),
    re_path('course/(?P<pk>[^/.]+)/tests', CourseTestsAPIView.as_view(), name='course-tests'),
    re_path('student/(?P<pk>[^/.]+)/recommendation', CourseRecommendationAPIView.as_view(), name='student-recommendation')
]
