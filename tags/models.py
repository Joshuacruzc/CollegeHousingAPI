from django.db import models


class Tag(models.Model):
    description = models.CharField(max_length=15)

    def __str__(self):
        return self.description
