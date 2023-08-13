import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, F, Q
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.tiku.models import TestPaper, LargeClass, SubClass, TotalScoreInterval, LargeScoreInterval, \
    SubScoreInterval, Subject, SurveyResult, Option
from apps.tiku.serializers import TestPaperSerializer, LargeClassSerializer, SubClassSerializer, \
    SubjectSerializer, SurveyResultSerializer, OptionSerializer, SurveyResultCreateSerializer, \
    OptionPartialUpdateSerializer, IsCompleteQuerySerializer, SurveyResultListSerializer
from apps.wechat.models import User


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
    filterset_fields = ('openid', 'completed')

    def get_serializer_class(self):
        if self.action == 'create':
            return SurveyResultCreateSerializer
        elif self.action == 'list':
            return SurveyResultListSerializer
        else:
            return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        openid = serializer.validated_data.get('openid')
        test_paper = serializer.validated_data.get('test_paper')
        phone = serializer.validated_data.get('phone')
        if SurveyResult.objects.filter(openid=openid, phone=phone, test_paper=test_paper, completed=False).exists():
            survey_result = SurveyResult.objects.filter(openid=openid, test_paper=test_paper, completed=False).first()
            serializer = SurveyResultSerializer(survey_result)
        else:
            user = User.objects.get(openid=openid)
            if user is None:
                return JsonResponse({
                    'status': 1,
                    'msg': '用户不存在，请先通过openid创建用户。'
                }, status=status.HTTP_400_BAD_REQUEST)
            self.perform_create(serializer)
            serializer.instance.user = user
            serializer.instance.save()
            serializer = SurveyResultSerializer(serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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

    @swagger_auto_schema(methods=['GET'], responses={200: SurveyResultSerializer})
    @action(methods=['GET'], detail=False, url_path=r'complete/(?P<id>\w+)')
    def complete(self, request, *args, **kwargs):
        try:
            instance: SurveyResult = self.queryset.get(pk=kwargs['id'])
        except ObjectDoesNotExist:
            return JsonResponse({
                    'status': 1,
                    'msg': '该测试不存在，请先确认id是否正确'
                }, status=status.HTTP_400_BAD_REQUEST)
        if instance.completed:
            return JsonResponse({
                    'status': 1,
                    'msg': '该测试已经完成，请不要重复提交'
                }, status=status.HTTP_400_BAD_REQUEST)
        large_class_sum = Option.objects.filter(
            servey_result=instance
        ).values(large_class_id=F('subject__large_class')).annotate(
            opt_score=Sum('opt_score')
        )
        total_result_score = instance.option_set.values('opt_score').aggregate(Sum('opt_score')).get('opt_score__sum')

        total_score_interval: TotalScoreInterval = TotalScoreInterval.objects.filter(
            test_paper=instance.test_paper,
            min_score__lte=total_result_score, max_score__gt=total_result_score
        ).first()
        max_score = instance.test_paper.subject_set.count() * 5
        result_dict = {
            "nickname": instance.user.name,
            "user_id": instance.user.id,
            "complete_time": (datetime.datetime.now() - instance.created).seconds,
            "total_score": max_score,
            "result_score": total_result_score,
            "total_grade": '' if total_score_interval is None else total_score_interval.grade,
            "total_description": '' if total_score_interval is None else total_score_interval.description
        }
        radar_data_sub_dict = {}
        radar_data_large_list = []
        large_class_list = []
        for item_1 in large_class_sum:
            radar_data_sub_list = []
            large_class_id = item_1.get('large_class_id')
            large_result_score = item_1.get('opt_score')
            large_class: LargeClass = LargeClass.objects.get(pk=large_class_id)
            sub_class_sum = Option.objects.filter(
                servey_result=instance,
                subject__large_class=large_class
            ).values(sub_class_id=F('subject__sub_class')).annotate(
                opt_score=Sum('opt_score')
            )
            large_score_interval: LargeScoreInterval = LargeScoreInterval.objects.filter(
                large_class=large_class,
                min_score__lte=large_result_score, max_score__gt=large_result_score
            ).first()
            large_max_class = large_class.subject_set.count() * 5
            sub_class_list = []
            for item_2 in sub_class_sum:
                sub_class_id = item_2.get('sub_class_id')
                sub_score = item_2.get('opt_score')
                sub_class: SubClass = SubClass.objects.get(pk=sub_class_id)
                sub_score_interval: SubScoreInterval = SubScoreInterval.objects.filter(
                    sub_class=sub_class,
                    min_score__lte=sub_score, max_score__gt=sub_score
                ).first()
                all_sub_interval = SubScoreInterval.objects.filter(sub_class=sub_class).all()
                sub_max_score = sub_class.subject_set.count() * 5
                grade_note_list = []
                for item3 in all_sub_interval:
                    grade_note_list.append(f"{item3.min_score}-{item3.max_score}属于{item3.grade}")
                sub_class_list.append({
                    "sub_class_id": sub_class_id,
                    "sub_class_name": sub_class.class_name,
                    "sub_total_score": sub_max_score,
                    "sub_result_score": sub_score,
                    "sub_class_grade": '' if sub_score_interval is None else sub_score_interval.grade,
                    "sub_class_grade_note": '，'.join(grade_note_list),
                    "description": '' if sub_score_interval is None else sub_score_interval.description
                })
                radar_data_sub_list.append({
                    "id": sub_class_id,
                    "name": sub_class.class_name,
                    "max_score": sub_max_score,
                    "score": sub_score,
                })
            large_class_list.append({
                "large_class_id": large_class_id,
                "large_class_name": large_class.class_name,
                "large_total_score": large_max_class,
                "large_result_score": large_result_score,
                "large_class_grade": '' if large_score_interval is None else large_score_interval.grade,
                "description": '' if large_score_interval is None else large_score_interval.description,
                "sub_class_list": sub_class_list
            })
            radar_data_large_list.append({
                "id": large_class_id,
                "name": large_class.class_name,
                "max_score": large_max_class,
                "score": large_result_score,
            })
            radar_data_sub_dict[large_class_id] = radar_data_sub_list
        result_dict['detail'] = large_class_list
        result_dict['radar_large_class'] = radar_data_large_list
        result_dict['radar_sub_class'] = radar_data_sub_dict
        instance.completed = True
        instance.results_json = result_dict
        instance.save()
        serializer = SurveyResultSerializer(instance)

        return JsonResponse(serializer.data)

    @swagger_auto_schema(methods=['GET'], serializer_or_field=IsCompleteQuerySerializer)
    @action(methods=['GET'], detail=False, url_path=r'is_complete')
    def is_complete(self, request, *args, **kwargs):
        openid = request.query_params.get('openid')
        try:
            instance: SurveyResult = self.queryset.filter(openid=openid, completed=False).first()
        except ObjectDoesNotExist:
            return
        if instance is None:
            return JsonResponse({"status": True, "tests": []}, status=status.HTTP_200_OK)
        options = instance.option_set.all()
        continue_option = instance.option_set.filter((Q(opt="") | Q(opt=None))).order_by('id').first()
        if continue_option is None:
            continue_option = instance.option_set.last()
        options_serializer = OptionSerializer(options, many=True)

        return JsonResponse(
            {
                "status": False, 'tests': options_serializer.data,
                'continue_id': continue_option.id,
                'id': instance.pk
            },
            status=status.HTTP_200_OK
        )


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

    def get_serializer_class(self):
        if self.action in ['update']:
            return OptionPartialUpdateSerializer
        else:
            return self.serializer_class

    def perform_update(self, serializer):
        option = serializer.instance
        if option.servey_result.completed:
            raise serializers.ValidationError('该选项的问卷已经完成了，无法继续修改。')
        opt = serializer.validated_data.get('opt')
        if opt is not None:
            serializer.validated_data['opt_score'] = option.subject.__getattribute__(self.key_map.get(opt))
            serializer.is_valid(raise_exception=True)
        serializer.save()
