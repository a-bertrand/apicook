from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import CategorySerializer
from apicook.cookie.models import Category
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
