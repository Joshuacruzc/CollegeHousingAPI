from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Owner(models.Model):
    # TODO use actual max length for a phone, add custom validator
    phone_number = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=32, null=True)


class Housing(models.Model):
    location = models.PointField()
    address = models.CharField(max_length=100)
    owned_by = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)


