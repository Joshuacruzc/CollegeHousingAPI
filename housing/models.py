from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.utils.safestring import mark_safe


class Owner(models.Model):
    # TODO use actual max length for a phone, add custom validator
    phone_number = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.user.__str__()


class Housing(models.Model):
    location = models.PointField()
    address = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images')

    def image_tag(self):
        return mark_safe(u'<img src="%s" />' % self.images.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.address
