from rest_framework import serializers
from .models import Article, Ingredient, Recipe, Shop, ShopList


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','name')


class IngredientSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=False)
    class Meta:
        model = Ingredient
        fields = ('id', 'article', 'quantity', 'weight')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredeints')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient)
        return recipe


class ShopSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = Shop
        fields = '__all__'


class ShopListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopList
        fields = '__all__'