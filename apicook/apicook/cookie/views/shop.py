from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import ShopSerializer
from apicook.cookie.models import Shop
from rest_framework.views import APIView


"""
    Generate random recipe list with excluded recipe
"""
class GenerateListShopRecipe(APIView):
    
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
                #Error TODO make beautiful response
                return Response()
            
        else:
            if not excluded_recipe:
                excluded_recipe = []
            shop = Shop()
            shop.save()
            shop.generate_random_recipe(number_recipe, excluded_recipe)

        data = ShopSerializer(shop).data
        return Response({**data})
