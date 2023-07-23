from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'test_paper', views.TestPaperViewSet)
# router.register(r'large_class', views.LargeClassViewSet)
# router.register(r'sub_class', views.SubClassViewSet)
# router.register(r'score_interval', views.ScoreIntervalViewSet)
# router.register(r'subject', views.SubjectViewSet)
router.register(r'survey_result', views.SurveyResultViewSet)
router.register(r'option', views.OptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("", views.index, name="index"),
]
