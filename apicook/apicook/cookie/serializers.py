from rest_framework import serializers

from .models import Article, Ingredient, Recipe


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Article
        fields = '__all__'


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Recipe
        fields = '__all__'