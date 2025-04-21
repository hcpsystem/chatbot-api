from django.db import models
from core.models import StateAbstract, TimestampAbstract


def settings_default_value():
    return {}


class User(StateAbstract, TimestampAbstract):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name='ID', editable=True, unique=True)
    to = models.CharField(max_length=100, blank=False, default='')
    from_id = models.CharField(max_length=100, blank=False, default='')
    name = models.CharField(max_length=70, blank=False, default='')
    wa_id = models.CharField(max_length=70, blank=False, default='')
    country = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    step = models.CharField(max_length=64)
    settings = models.JSONField(default=settings_default_value)

    class Meta:
        db_table = 'users'


class Session(StateAbstract, TimestampAbstract):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name='ID', editable=True, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='receiver',
        null=True,
        blank=True,
    )
    token = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'sessions'
