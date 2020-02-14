from rest_framework import serializers
from .models import Article, Ingredient, Recipe, ShoppingRecipeList, ShoppingIngredientList, Step
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','name')


class IngredientSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=False)
    class Meta:
        model = Ingredient
        fields = ('id', 'article', 'quantity', 'measure_type')


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    steps = StepSerializer(many=True)

    image_url_aze = serializers.SerializerMethodField('get_image_url') 

    class Meta:
        model = Recipe
        fields = ('id', 'categories', 'ingredients', 'steps', 'title', 'text', 'image', 'owner', 'image_url_aze')

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient)
        return recipe
    
    def get_image_url(self, obj):
        return obj.image.url


class ShopSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = ShoppingRecipeList
        fields = '__all__'


class ShopListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingIngredientList
        fields = '__all__'
