from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import ShopSerializer, RecipeSerializer
from apicook.cookie.models import Shop
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
    
    def get(self, request, shop_id = None, format=None, wanted_recipes=None):
        asker_user = User.objects.get(pk=request.user.id)
        if wanted_recipes:
            recipes = Shop.generate_random_recipe(len(wanted_recipes), wanted_recipes)
        else:
            asked_number_recipe = request.GET.get('number_recipe')
            recipes = Shop.generate_random_recipe(asked_number_recipe)

        return Response(
            RecipeSerializer(recipes, many=True).data
        )

    def post(self, request):
        asker_user = User.objects.get(pk=request.user.id)
        recipe_list = request.POST.get('recipes')

        shop = Shop()
        shop.recipes = Recipe.objects.filter(id__in=recipe_list).all()
        shop.save()
        shop.contributors.set([asker_user])
        shop.save()


        """
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
