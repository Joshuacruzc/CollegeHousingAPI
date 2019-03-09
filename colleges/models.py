from django.contrib.gis.db import models


class College(models.Model):
    location = models.PointField()
    name = models.CharField(max_length=100)
