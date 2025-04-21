from rest_framework import serializers

from users.models import User


class AppService:
    def __init__(
            self,
            request=None,
            serializer: serializers.ModelSerializer | serializers.Serializer = None,
            user: User = None,
            logged: User = None
    ):
        self.request = request
        self.serializer = serializer
        self.user = user
        self.logged = logged


class AppGateway:
    def __init__(self, logged: User = None):
        self.logged = logged


class AppFactory:
    def __init__(self, logged: User = None):
        self.logged = logged
