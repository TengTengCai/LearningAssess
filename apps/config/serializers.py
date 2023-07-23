
from rest_framework import serializers

from apps.config.models import CourseInfo, Config


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ['xetong_address']


class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInfo
        fields = ['title', 'url', 'image']
        # fields = '__all__'
