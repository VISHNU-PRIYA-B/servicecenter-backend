from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(jwt_cookie, name="dispatch")
class PrivateGraphQLView(GraphQLView):
    """
    GraphQL view that ensures jwt_cookie decorator runs during dispatch,
    so info.context.user gets populated from the Authorization header.
    """
    pass
