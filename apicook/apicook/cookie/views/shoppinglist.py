from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.models import  Shop, Article, ShopList
from apicook.cookie.serializers import ShopListSerializer
from rest_framework.views import APIView

"""
    Get ingredient list
"""
class ShoppingListRecipe(APIView):

    def get(self, request, shop_id = None):
        shop = Shop.objects.get(pk=shop_id)

        return self._get_list_to_buy(shop)

    def _get_list_to_buy(self, shop):
        
        shop_list = shop.list_content.all()

        formated_ingredients = []
        for ingredient in shop_list:
            formated_ingredient = {
                'id': ingredient.id,
                'name': ingredient.article.name,
                'bought_value': ingredient.bought_value,
                'bought_status': ingredient.bought_status,
                'quantity': ingredient.total_quantity,
                'weight': ingredient.total_weight,
            }
            formated_ingredients.append(formated_ingredient)   

        return Response(
            formated_ingredients
        )

class ShoppingListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShopList.objects.all()
    serializer_class = ShopListSerializer
