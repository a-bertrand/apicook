from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import RecipeSerializer
from apicook.cookie.models import Recipe
from rest_framework.views import APIView


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)