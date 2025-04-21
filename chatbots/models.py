from django.db import models
from core.models import StateAbstract, TimestampAbstract
from users.models import User


# Create your models here.

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


class Response(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name='ID', editable=True, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='chatbot_responses',
        null=True,
        blank=True,
    )
    question_id = models.CharField(max_length=50, null=True, blank=True)
    question_text = models.TextField(null=True, blank=True)
    selected_option = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    is_bot = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        who = "Bot" if self.is_bot else "User"
        return f"{who}: {self.message[:40]}"

    class Meta:
        db_table = 'responses'
