import graphene
import graphql_jwt

import cookbook.ingredients.schema
import users.schema


class Query(cookbook.users.schema.Query, cookbook.ingredients.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(cookbook.users.schema.Mutation, cookbook.ingredients.schema.Mutation):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)