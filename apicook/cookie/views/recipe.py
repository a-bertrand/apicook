from rest_framework import viewsets, filters
from rest_framework.response import Response
from apicook.cookie.serializers import RecipeSerializer
from apicook.cookie.models import Recipe
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
import json 


class RecipeViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        title = request.GET.get('title')
        categories = json.loads(request.GET.get('categories'))
        
        recipes = Recipe.objects.filter(title__icontains=title)
        if len(categories) != 0:
            oldRecipes = Recipe.objects.filter(title__icontains=title)
            recipes = []
            for recipe in oldRecipes:
                recipes_categories = [ recipeId for recipeId in recipe.categories.values_list('id', flat=True)]
                categories_in_recipes_categories = self.array_subset_array(categories, recipes_categories)
                if categories_in_recipes_categories:
                    recipes.append(recipe)

        return Response(
            RecipeSerializer(
                recipes,
                many=True
            ).data
        )

    def array_subset_array(self, array1, array2):
        for id in array1: 
            if id not in array2:
                return False
        return True