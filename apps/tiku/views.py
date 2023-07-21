from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from apps.tiku.models import TestPaper, LargeClass, SubClass, ScoreInterval, Subject, SurveyResult, Option
from apps.tiku.serializers import TestPaperSerializer, LargeClassSerializer, SubClassSerializer, \
    ScoreIntervalSerializer, SubjectSerializer, SurveyResultSerializer, OptionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TestPaperViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TestPaper.objects.all()
    serializer_class = TestPaperSerializer
    permission_classes = [permissions.AllowAny]


class LargeClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = LargeClass.objects.all()
    serializer_class = LargeClassSerializer
    permission_classes = [permissions.AllowAny]


class SubClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SubClass.objects.all()
    serializer_class = SubClassSerializer
    permission_classes = [permissions.AllowAny]


class ScoreIntervalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ScoreInterval.objects.all()
    serializer_class = ScoreIntervalSerializer
    permission_classes = [permissions.AllowAny]


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]


class SurveyResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SurveyResult.objects.all()
    serializer_class = SurveyResultSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('openid', 'phone')

    def perform_create(self, serializer):
        serializer.save()
        test_paper = serializer.data.get('test_paper')
        survey_id = serializer.data.get('id')
        subject_list = Subject.objects.filter(test_paper=test_paper, ).all()
        for subject in subject_list:
            if not Option.objects.filter(servey_result=survey_id, subject=subject.pk).exists():
                Option(
                    servey_result=serializer.instance,
                    subject=subject).save()


class OptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    key_map = {
        'a_ans': 'a_score',
        'b_ans': 'b_score',
        'c_ans': 'c_score',
        'd_ans': 'd_score',
        'e_ans': 'e_score',
    }

    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [permissions.AllowAny]

    def perform_update(self, serializer):
        option = serializer.instance
        opt = serializer.validated_data.get('opt')
        if opt is not None:
            serializer.validated_data['opt_score'] = option.subject.__getattribute__(self.key_map.get(opt))
            serializer.is_valid(raise_exception=True)
        serializer.save()
