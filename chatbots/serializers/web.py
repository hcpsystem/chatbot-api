from rest_framework import serializers


class WebLoginValidatorSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    name = serializers.CharField(required=True)
