from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import ShopSerializer, RecipeSerializer
from apicook.cookie.models import ShoppingRecipeList, Recipe
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

"""
    Generate random recipe list with excluded recipe

    number_recipe
    excluded_recipe
    generate = FALSE

    si shop_id & generate FALSE juste GET
    si shop_id & generate TRUE re-generation
    sinon creation

"""
class GenerateListShopRecipe(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        asker_user = User.objects.get(pk=request.user.id)
        number_recipe = request.GET.get('number_recipe')
        wanted_recipes = request.GET.get('wanted_recipes')
        if wanted_recipes:
            arrayOfRecipeIds = wanted_recipes.split(',')
            old_recipes = Recipe.objects.filter(id__in=arrayOfRecipeIds).all()
            recipes = ShoppingRecipeList.generate_random_recipe(number_recipe, arrayOfRecipeIds)
        else:
            recipes = ShoppingRecipeList.generate_random_recipe(number_recipe)

        return Response(
            RecipeSerializer(recipes, many=True).data
        )


    def post(self, request):
        asker_user = User.objects.get(pk=request.user.id)
        recipes = request.data

        recipe_id_list = [recipe.get('id') for recipe in recipes]

        shopping_recipe_list = ShoppingRecipeList()
        shopping_recipe_list.save()
        shopping_recipe_list.recipes.set(Recipe.objects.filter(id__in=recipe_id_list).all())
        shopping_recipe_list.contributors.set([asker_user])
        shopping_recipe_list.save()

        return Response({'shop-list-id': shopping_recipe_list.id})
        """

        , format=None):
        asked_number_recipe = request.GET.get('number_recipe')
        wanted_recipes = request.GET.get('
        asked_excluded_recipe = []
        if (request.GET.get('excluded_recipe')) :
            asked_excluded_recipe = list(map(int, request.GET.get('excluded_recipe').split(',')))
        
        want_generate = request.GET.get('generate') == 'true' if request.GET.get('generate') else False

        if shop_id:
            try:
                shop = Shop.objects.get(pk=shop_id, contributors__in=[asker_user])
                if want_generate:
                    shop.generate_random_recipe(asked_number_recipe, asked_excluded_recipe)
            except Exception as e:
                #Error TODO make beautiful response
                return Response()
            
        else:
            shop = Shop()
            shop.save()
            shop.contributors.set([asker_user])
            shop.save()
            shop.generate_random_recipe(asked_number_recipe, asked_excluded_recipe)
        
        shop.generate_shopping_list()

        data = ShopSerializer(shop).data
        print(data)
        return Response({**data})
        """
