from django.contrib.auth import get_user_model
from rest_framework import serializers

from housing.models import Housing, Owner, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'email')


class OwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Owner
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class HousingSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    owner = OwnerSerializer(many=False)
    images = ImageSerializer(many=True)

    class Meta:
        model = Housing
        fields = "__all__"


