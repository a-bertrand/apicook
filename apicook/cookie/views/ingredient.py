from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import IngredientSerializer
from apicook.cookie.models import Ingredient
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
