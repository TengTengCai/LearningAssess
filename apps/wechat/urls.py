from django.urls import path, include
from rest_framework import routers

from apps.wechat import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path("login", views.login, name="login"),
]
