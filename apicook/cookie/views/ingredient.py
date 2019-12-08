from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import IngredientSerializer
from apicook.cookie.models import Ingredient


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
