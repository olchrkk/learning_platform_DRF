from rest_framework import routers
from django.urls import path, include

from users.endpoinds import UserViewSet

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
