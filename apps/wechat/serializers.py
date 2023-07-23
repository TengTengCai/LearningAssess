from rest_framework import serializers

from apps.wechat.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['openid', 'name', 'sex', 'age', 'grade', 'phone']
        # fields = '__all__'
