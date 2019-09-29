from rest_framework import viewsets, filters
from rest_framework.response import Response
from .serializers import ArticleSerializer, IngredientSerializer, RecipeSerializer, ShopSerializer
from .models import Article, Ingredient, Recipe, Shop
from rest_framework.views import APIView

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class ListShopRecipe(APIView):
    
    def get(self, request, id_shop = None, format=None):
        number_recipe = request.GET.get('number_recipe')
        excluded_recipe = []
        if (request.GET.get('excluded_recipe')) :
            excluded_recipe = list(map(int, request.GET.get('excluded_recipe').split(',')))
        
        generate = request.GET.get('generate') == 'true' if request.GET.get('generate') else False

        if id_shop:
            try:
                shop = Shop.objects.get(pk=id_shop)
                if generate:
                    shop.generate_random_recipe(number_recipe, excluded_recipe)
            except Exception as e:
                print(str(e))
                return Response()
            
        else:
            if not excluded_recipe:
                excluded_recipe = []
            shop = Shop()
            shop.save()
            shop.generate_random_recipe(number_recipe, excluded_recipe)

        data = ShopSerializer(shop).data
        return Response({**data})
