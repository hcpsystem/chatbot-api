from django.db import models
from core.models import StateAbstract, TimestampAbstract

def settings_default_value():
    return {}


class Question(StateAbstract, TimestampAbstract):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name='ID', editable=True, unique=True)
    flow_id = models.CharField(unique=True, blank=False, max_length=50)
    parent_id = models.CharField(null=True, max_length=50)
    is_options = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    name = models.TextField()
    label = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    content_sid = models.CharField(max_length=255, blank=True, null=True)
    settings = models.JSONField(default=settings_default_value)

    class Meta:
        db_table = 'questions'


class Response(StateAbstract, TimestampAbstract):
    user_id = models.CharField(max_length=50, null=True, blank=True)
    question_id = models.CharField(max_length=50, null=True, blank=True)
    question_text = models.TextField(null=True, blank=True)
    selected_option = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    is_bot = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'responses'