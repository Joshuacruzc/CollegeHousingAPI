from rest_framework import viewsets

from colleges.models import College
from colleges.serializers import CollegeSerializer


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
