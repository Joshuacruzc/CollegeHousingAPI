import graphene
from graphene_django import DjangoObjectType

from housing.models import Housing
from tags.models import Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class CreateTag(graphene.Mutation):
    tag = graphene.Field(TagType)

    class Arguments:
        housing_id = graphene.Int(required=True)
        description = graphene.String(required=True)

    def mutate(self, info, housing_id, description):
        housing = Housing.objects.get(pk=housing_id)
        if not housing:
            raise Exception('Invalid ID for Housing')

        tag = Tag.objects.create(housing=housing, description=description)

        return CreateTag(tag=tag)


class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()

