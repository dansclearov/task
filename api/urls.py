from django.urls import path, include

from .views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TodoViewSet, basename='todo')
urlpatterns = [
    path('', include(router.urls)),
]