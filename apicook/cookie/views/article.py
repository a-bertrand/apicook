from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import ArticleSerializer
from apicook.cookie.models import Article
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
