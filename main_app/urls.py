
from django.urls import path
from .views import LandingPageView
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path("graphql", GraphQLView.as_view(graphiql=True)),

    # Add other URLs as needed
]
