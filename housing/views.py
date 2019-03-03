from django.http import HttpResponse
from rest_framework import viewsets

from housing.models import Image, Housing
from housing.serializers import HousingSerializer


class HousingViewSet(viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer


def upload_image(request):
    files = request.FILES['photo']
    files = files.decode('base64')
    Image(image=files, Housing=Housing.objects.all().first()).save()
    return HttpResponse('bops')
