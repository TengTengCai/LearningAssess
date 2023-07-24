
from rest_framework import serializers

from apps.config.models import CourseInfo, Config, Article


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ['index_image', 'xetong_address', 'shop_address', 'evaluation_image']


class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInfo
        fields = ['title', 'url', 'image']
        # fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image', 'a_type', 'url']
