from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.models import  ShoppingRecipeList, Article, ShoppingIngredientList
from apicook.cookie.serializers import ShopListSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


"""
    Get ingredient list
"""
class ShoppingListRecipe(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, shop_id = None):
        if shop_id:
            asker_user = User.objects.get(pk=request.user.id)
            shop = ShoppingRecipeList.objects.get(pk=shop_id, contributor__in=asker_user)

            return self._get_list_to_buy(shop)
        else :
            # Get all shop list
            formated_shops =  []
            shops = ShoppingRecipeList.objects.get(contributor__in=asker_user).order_by('-created_at')
            for shop in shops.all():
                formated_shop = {
                    'id': shop.id,
                    'created_at': shop.created_at
                }
            formated_shops.append(formated_shop) 
            return Response (
                formated_shops
            )

    def _get_list_to_buy(self, shop):
        
        shop_list = shop.list_content.all()

        formated_ingredients = []
        for ingredient in shop_list:
            formated_ingredient = {
                'id': ingredient.id,
                'name': ingredient.article.name,
                'bought_value': ingredient.bought_value,
                'bought_status': ingredient.bought_status,
                'measure_type': ingredient.measure_type,
                'quantity': ingredient.total_quantity,
            }
            formated_ingredients.append(formated_ingredient)   

        return Response(
            formated_ingredients
        )

class ShoppingListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShoppingIngredientList.objects.all()
    serializer_class = ShopListSerializer
