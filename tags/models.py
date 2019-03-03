from django.db import models


class Tag(models.Model):
    description = models.CharField(max_length=15)
