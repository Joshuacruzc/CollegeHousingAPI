import graphene
import graphql_geojson
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.db.models import Q
from graphene_django import DjangoObjectType
from graphql_geojson import GeoJSONType

from .models import Housing, Owner


class OwnerType(DjangoObjectType):
    class Meta:
        model = Owner


class HousingType(GeoJSONType):
    def resolve_images(self, context):
        return context.context._current_scheme_host + self.images.url

    class Meta:
        model = Housing
        geojson_field = 'location'


class Query(graphene.ObjectType):
    houses = graphene.List(
        HousingType,
        search=graphene.String(),
        ref_location=graphql_geojson.Geometry(),
        distance=graphene.Int(),
    )
    house = graphene.Field(HousingType, id=graphene.Int())
    owners = graphene.List(
        OwnerType,
        search=graphene.String()
    )
    owner = graphene.Field(OwnerType, id=graphene.Int())

    def resolve_houses(self, info, search=None, distance=10, ref_location=None, **kwargs):
        houses = Housing.objects.filter(**kwargs)
        if ref_location:
            houses = houses.filter(location__distance_lte=(ref_location, D(km=distance)))\
                .annotate(distance=Distance('location', ref_location)).order_by('distance')

        if search:
            houses = houses.filter(
                Q(address__icontains=search) |
                Q(tags__description__icontains=search) |
                Q(owner__company_name__icontains=search)
            )
        return houses

    def resolve_house(self, info, id):
        house = Housing.objects.get(pk=id)
        return house

    def resolve_owners(self, info, search=None, **kwargs):
        owners = Owner.objects.filter(**kwargs)
        if search:
            if search:
                Owner.objects.filter(
                    Q(name__icontains=search)
                )
        return owners

    def resolve_owner(self, info, id):
        owner = Owner.objects.get(pk=id)
        return owner


class CreateHousing(graphene.Mutation):
    housing = graphene.Field(HousingType)

    class Arguments:
        address = graphene.String()
        location = graphql_geojson.Geometry()
        owner_id = graphene.Int()

    def mutate(self, info, **kwargs):
        # TODO Get owner from context instead
        housing = Housing(**kwargs)
        housing.save()

        return CreateHousing(housing=housing)

 
class CreateOwner(graphene.Mutation):
    owner = graphene.Field(OwnerType)

    class Arguments:
        user_id = graphene.Int()
        phone_number = graphene.String()
        company_name = graphene.String()

    def mutate(self, info, **kwargs):
        # TODO Get user from context instead
        owner = Owner(**kwargs)
        owner.save()
        return CreateOwner(owner=owner)


class Mutation(graphene.ObjectType):
    create_housing = CreateHousing.Field()
    create_owner = CreateOwner.Field()
