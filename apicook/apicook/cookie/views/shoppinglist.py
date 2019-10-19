from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.models import  Shop, Article, ShopList
from rest_framework.views import APIView

"""
    Get ingredient list
"""
class ShoppingListRecipe(APIView):

    def get(self, request, shop_id = None):
        shop = Shop.objects.get(pk=shop_id)
        is_bought = request.GET.get('is_bought')
        if not is_bought:
            is_bought = False
       
        return self._get_list_to_buy(is_bought, shop)

    def _get_list_to_buy(self, is_bought, shop):
        
        shop_list = ShopList.objects.filter(shop_id=shop.id, is_bought=is_bought).prefetch_related('ingredients').first()

        formated_ingredients = []
        import pdb; pdb.set_trace()

        for ingredient in shop_list.ingredients:
            formated_ingredient = {
                'name': ingredredient.article.name,
                'quantity': ingredient.quantity,
                'weight': ingredient.weight,
            }
            formated_ingredients.append(formated_ingredient)   

        return Response(
            formated_ingredients
        )
