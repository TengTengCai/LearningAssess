import logging
from urllib.parse import urlparse

from rest_framework import serializers

from LearningAssess.settings import OSS_CDN_NETLOC
from apps.tiku.models import TestPaper, LargeClass, SubClass, Subject, SurveyResult, Option

logger = logging.getLogger(__name__)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
        fields = '__all__'


class TestPaperSerializer(serializers.ModelSerializer):
    desc_url = serializers.SerializerMethodField(read_only=True, method_name='get_desc_url')
    subject_set = SubjectSerializer(many=True, read_only=True)

    def get_desc_url(self, test_paper):
        try:
            o = urlparse(test_paper.desc_url.url)
            return o._replace(netloc=OSS_CDN_NETLOC).geturl()
        except Exception as e:
            logger.exception(e)
            return ""
        # request = self.context.get('request')
        # if test_paper is None:
        #     return ''
        # try:
        #     if not hasattr(test_paper.desc_url, 'url'):
        #         return ''
        # except ValueError:
        #     return ''
        # return request.build_absolute_uri(test_paper.desc_url.url)

    class Meta:
        model = TestPaper
        # fields = ['id', 'paper_name', 'description', 'subjects_set']
        fields = '__all__'


class LargeClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = LargeClass
        # fields = ['id', 'test_paper', 'class_name', 'description']
        fields = '__all__'


class SubClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubClass
        # fields = ['id', 'class_name', 'large_class', 'description']
        fields = '__all__'


# class ScoreIntervalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScoreInterval
#         # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
#         fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Option
        # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
        fields = '__all__'


class OptionPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['opt']
        # fields = '__all__'


class SurveyResultSerializer(serializers.ModelSerializer):
    option_set = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyResult
        # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
        fields = '__all__'


class SurveyResultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResult
        fields = ['test_paper', 'openid', 'phone', 'college_score', 'school_level']


class SurveyResultListSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = SurveyResult
        # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
        fields = '__all__'


class IsCompleteQuerySerializer(serializers.Serializer):
    openid = serializers.CharField(required=True)
