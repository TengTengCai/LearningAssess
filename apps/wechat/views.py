from django.http import JsonResponse
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from wechatpy import WeChatClient


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
    client = WeChatClient('wx337b946a0050fe3c', 'd66a7e7b7afa2874ce6a13bf2b6898c3')
    # ass_token = client.fetch_access_token()
    data = client.wxa.code_to_session(code)
    # user = client.user.get(data.get('openid'))
    return JsonResponse({"openid": data.get('openid')})


# class Login(APIView):
#     authentication_classes = []
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)
