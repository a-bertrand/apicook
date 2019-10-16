from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.models import  Shop, Article
from rest_framework.views import APIView


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

