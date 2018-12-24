from django.db import models


class Tag(models.Model):
    description = models.CharField(max_length=15)
    housing = models.ForeignKey('housing.Housing', related_name='tags', on_delete=models.CASCADE)

