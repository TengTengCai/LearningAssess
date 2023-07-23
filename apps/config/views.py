from django.http import JsonResponse

from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes

from apps.config.models import CourseInfo, Config
from apps.config.serializers import CourseInfoSerializer, ConfigSerializer


# Create your views here.
@swagger_auto_schema(method='GET')
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def config(request):
    config_obj = Config.objects.first()
    serializer = ConfigSerializer(config_obj)
    return JsonResponse(serializer.data)


class CourseInfoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CourseInfo.objects.all()
    serializer_class = CourseInfoSerializer
    permission_classes = [permissions.AllowAny]
    # pagination_class = MyPageNumberPagination
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('openid', 'phone')
