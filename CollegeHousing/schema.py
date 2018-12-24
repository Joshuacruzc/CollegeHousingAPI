import graphene
import graphql_jwt

import housing.schema
import users.schema
import tags.schema


class Query(users.schema.Query, housing.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, housing.schema.Mutation, tags.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)