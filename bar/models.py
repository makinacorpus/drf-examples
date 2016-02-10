from django.db import models


class Bar(models.Model):
    name = models.SlugField(unique=True, max_length=255, null=True)
    doc = models.FileField(null=True, blank=True)
