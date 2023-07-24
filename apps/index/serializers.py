from rest_framework import serializers


class ProfileQuerySerializer(serializers.Serializer):
    openid = serializers.CharField()
