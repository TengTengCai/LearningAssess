from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets, permissions

from apps.tiku.models import TestPaper, LargeClass, SubClass, ScoreInterval, Subject
from apps.tiku.serializers import TestPaperSerializer, LargeClassSerializer, SubClassSerializer, \
    ScoreIntervalSerializer, SubjectSerializer


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
