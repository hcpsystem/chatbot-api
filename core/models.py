from django.db import models


class TimestampAbstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StateAbstract(models.Model):
    # TODO Use options of constants
    status = models.CharField(max_length=25, default='active')
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
