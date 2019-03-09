from rest_framework import serializers

from colleges.models import College


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

