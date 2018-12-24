import graphene
from django.contrib.auth.models import User
from django.db.models import Q
from graphene_django import DjangoObjectType

from users.schema import UserType
from .models import Housing, Owner


class OwnerType(DjangoObjectType):
    class Meta:
        model = Owner


class HousingType(DjangoObjectType):
    class Meta:
        model = Housing


class Query(graphene.ObjectType):
    houses = graphene.List(HousingType, search=graphene.String())
    house = graphene.Field(HousingType, id=graphene.Int())
    owners = graphene.List(OwnerType, search=graphene.String())
    owner = graphene.Field(OwnerType, id=graphene.Int())

    def resolve_houses(self, info, search=None, **kwargs):
        houses = Housing.objects.filter(**kwargs)
        if search:
            houses.objects.filter(
                Q(location__icontains=search) |
                Q(tags__description__icontains=search)
                # TODO add owner name as search parameter
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


class CreateHousing(graphene.Mutation):
    housing = graphene.Field(HousingType)

    class Arguments:
        location = graphene.String()

    def mutate(self, info, location):
        user = info.context.user.owner or None
        housing = Housing(location=location, owned_by=user)
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
