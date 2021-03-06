from django.contrib.postgres.fields import JSONField
from django.db import models

from organization.models import BaseTemplate
from misc.models import Content


class Preboarding(BaseTemplate):
    content = models.ManyToManyField(Content)
    form = JSONField(null=True, blank=True)
    picture = models.FileField(null=True)

    def __str__(self):
        return self.name
