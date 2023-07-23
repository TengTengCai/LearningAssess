from django.urls import path, include
from rest_framework import routers

from apps.config import views

router = routers.DefaultRouter()
router.register(r'course_info', views.CourseInfoViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path("cfg/", views.config, name="config"),
]
