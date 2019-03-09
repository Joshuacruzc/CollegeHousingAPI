from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import viewsets

from colleges.models import College
from housing.models import Image, Housing
from housing.serializers import HousingSerializer


class HousingViewSet(viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer

    def get_queryset(self):
        queryset = Housing.objects.all()
        distance = self.request.query_params.get('distance')
        college_id = self.request.query_params.get('college_id')
        ref_location = None
        search = self.request.query_params.get('search')

        if college_id:
            ref_location = College.objects.get(pk=college_id).location
        if distance and ref_location:
            queryset = queryset.filter(location__distance_lte=(ref_location, D(km=distance))) \
                .annotate(distance=Distance('location', ref_location)).order_by('distance')
        if search:
            queryset = queryset.filter(
                Q(address__icontains=search) |
                Q(owner__company_name__icontains=search)
            )
        return queryset


def upload_image(request):
    files = request.FILES['photo']
    files = files.decode('base64')
    Image(image=files, Housing=Housing.objects.all().first()).save()
    return HttpResponse('bops')
