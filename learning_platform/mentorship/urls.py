from rest_framework import routers
from django.urls import path, include, re_path

from mentorship.endpoinds import StudentViewSet, TeacherViewSet, TeacherGroupViewSet, SpecificationTeacherAPIView,\
    StudentsAndTeachersAPIView


router = routers.SimpleRouter()
router.register(r'student', StudentViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'teachergroup', TeacherGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path('specification/(?P<pk>[^/.]+)/teacher', SpecificationTeacherAPIView.as_view(), name='specification-teacher'),
    path('students-teachers-list/', StudentsAndTeachersAPIView.as_view(), name='students-teachers-list')
]
