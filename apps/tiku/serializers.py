from rest_framework import serializers

from apps.tiku.models import TestPaper, LargeClass, SubClass, Subject, SurveyResult, Option


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
        fields = '__all__'


class TestPaperSerializer(serializers.ModelSerializer):
    subject_set = SubjectSerializer(many=True, read_only=True)

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
        fields = ['servey_result', 'subject', 'opt', 'opt_score']
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
    class Meta:
        model = SurveyResult
        # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
        fields = '__all__'
