from django.http import JsonResponse
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from apps.config.models import Config, CourseInfo, Article
from apps.config.serializers import ConfigSerializer, CourseInfoSerializer, ArticleSerializer
from apps.index.serializers import ProfileQuerySerializer
from apps.tiku.models import SurveyResult
from apps.tiku.serializers import SurveyResultListSerializer


# Create your views here.
class IndexView(APIView):
    permission_classes = [permissions.AllowAny]

    # noinspection PyTypeChecker
    @swagger_auto_schema()
    def get(self, request, format=None):
        config_obj = Config.objects.first()
        config_serializer = ConfigSerializer(config_obj)

        course_info_obj = CourseInfo.objects.all()
        course_info_serializer = CourseInfoSerializer(course_info_obj, many=True)

        article_obj = Article.objects.filter(a_type=Article.ArticleType.CUR).all()
        article_serializer = ArticleSerializer(article_obj, many=True)
        content = {
            'config': config_serializer.data,
            'course_info': course_info_serializer.data,
            'article': article_serializer.data
        }
        return JsonResponse(content)


class ProfileView(APIView):
    permission_classes = [permissions.AllowAny]

    # noinspection PyTypeChecker
    @swagger_auto_schema(query_serializer=ProfileQuerySerializer)
    def get(self, request, format=None):
        openid = request.data.get('openid')

        sr_obj = SurveyResult.objects.filter(openid=openid, completed=True).all()
        sr_serializer = SurveyResultListSerializer(sr_obj, many=True)

        his_article_obj = Article.objects.filter(a_type=Article.ArticleType.HIS).all()
        his_article_serializer = ArticleSerializer(his_article_obj, many=True)

        com_article_obj = Article.objects.filter(a_type=Article.ArticleType.COM).all()
        com_article_serializer = ArticleSerializer(com_article_obj, many=True)
        content = {
            'survey_result': sr_serializer.data,
            'his_article': his_article_serializer.data,
            'com_article': com_article_serializer.data,
        }
        return JsonResponse(content)
