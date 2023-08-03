import requests
from django.http import JsonResponse
from django_filters import rest_framework as filters
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, viewsets, mixins, status
from rest_framework.decorators import api_view, permission_classes
from wechatpy import WeChatClient

from LearningAssess.settings import MINI_PROGRAM
from apps.wechat.models import User
from apps.wechat.serializers import UserSerializer


# Create your views here.
@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    # 构造的请求体为 dict 类型
    type=openapi.TYPE_OBJECT,
    # 构造的请求体中 必填参数 列表
    required=['code'],
    # 自定义请求体 ， key为请求参数名称，值为参数描述
    properties={
        'code': openapi.Schema(type=openapi.TYPE_STRING, description='微信code'),
    }
))
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    code = request.data.get('code')
    try:
        client = WeChatClient(MINI_PROGRAM['AppID'], MINI_PROGRAM['AppSecret'])
        data = client.wxa.code_to_session(code)
    except Exception as e:
        return JsonResponse(
            {
                'status': 1,
                'msg': 'failed',
                'data': {"err": e.__str__()}
            }, status=status.HTTP_400_BAD_REQUEST
        )

    return JsonResponse(
        {
            'status': 0,
            'msg': 'success',
            'data': {"openid": data.get('openid')}
        }
    )
@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    # 构造的请求体为 dict 类型
    type=openapi.TYPE_OBJECT,
    # 构造的请求体中 必填参数 列表
    required=['code'],
    # 自定义请求体 ， key为请求参数名称，值为参数描述
    properties={
        'code': openapi.Schema(type=openapi.TYPE_STRING, description='微信code'),
    }
))
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_phone_num(request):
    code = request.data.get('code')
    try:
        client = WeChatClient(MINI_PROGRAM['AppID'], MINI_PROGRAM['AppSecret'])
        # access_token_resp = requests.get(
        #     f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&'
        #     f'appid={MINI_PROGRAM["AppID"]}&secret={MINI_PROGRAM["AppSecret"]}')
        # access_token_resp.raise_for_status()
        # access_token = access_token_resp.json().get('access_token')
        resp = requests.post(
            f'https://api.weixin.qq.com/wxa/business/getuserphonenumber?access_token={client.access_token}',
            json={
                "code": code
            }
        )
        resp.raise_for_status()
    except Exception as e:
        return JsonResponse(
            {
                'status': 1,
                'msg': 'failed',
                'data': {"err": e.__str__()}
            }, status=status.HTTP_400_BAD_REQUEST
        )

    return JsonResponse(
        {
            'status': 0,
            'msg': 'success',
            'data': resp.json()
        }
    )

class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('openid', 'phone')

