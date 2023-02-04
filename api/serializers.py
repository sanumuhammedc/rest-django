from rest_framework import serializers


class RestLogin(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
