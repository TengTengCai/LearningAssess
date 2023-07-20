from rest_framework import serializers

from apps.tiku.models import TestPaper, LargeClass, SubClass, ScoreInterval, Subject


class TestPaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestPaper
        # fields = ['id', 'paper_name', 'description']
        fields = '__all__'


class LargeClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LargeClass
        # fields = ['id', 'test_paper', 'class_name', 'description']
        fields = '__all__'


class SubClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubClass
        # fields = ['id', 'class_name', 'large_class', 'description']
        fields = '__all__'


class ScoreIntervalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScoreInterval
        # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
        fields = '__all__'


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        # fields = ['id', 'sub_class', 'min_score', 'max_score', 'description']
        fields = '__all__'
