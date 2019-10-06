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
    
    def get(self, request, shop_id = None, format=None):
        number_recipe = request.GET.get('number_recipe')
        excluded_recipe = []
        if (request.GET.get('excluded_recipe')) :
            excluded_recipe = list(map(int, request.GET.get('excluded_recipe').split(',')))
        
        generate = request.GET.get('generate') == 'true' if request.GET.get('generate') else False

        if shop_id:
            try:
                shop = Shop.objects.get(pk=shop_id)
                if generate:
                    shop.generate_random_recipe(number_recipe, excluded_recipe)
            except Exception as e:
                #Error TODO
                return Response()
            
        else:
            if not excluded_recipe:
                excluded_recipe = []
            shop = Shop()
            shop.save()
            shop.generate_random_recipe(number_recipe, excluded_recipe)

        data = ShopSerializer(shop).data
        return Response({**data})


class ShoppingListRecipe(APIView):
    def get(self, request, shop_id = None):
        shop = Shop.objects.get(pk=shop_id)

        ingredients = shop.generate_shopping_list()

        formated_ingredients = []
        for ingredient in ingredients:
            formated_ingredient = {
                'name': Article.objects.get(pk=ingredient['article_id']).name,
                'quantity': ingredient['quantity'],
                'weight': ingredient['weight'],
            }
            formated_ingredients.append(formated_ingredient)   

        return Response(
            formated_ingredients
        )

