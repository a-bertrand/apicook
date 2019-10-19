from django.db import models
from .recipe import Recipe
from .ingredient import Ingredient
from django.db.models import Sum


class Shop (models.Model): 
    recipes = models.ManyToManyField(
        "Recipe",
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.created)

    def generate_random_recipe(self, number_of_recipe, excluded_ids = []):
        if number_of_recipe == None:
            number_of_recipe = 1

        self.recipes.clear()

        recipes = Recipe.objects.order_by("?").exclude(id__in=excluded_ids)[:int(number_of_recipe)]

        for recipe in recipes:
            self.recipes.add(recipe)
        self.save()

    def generate_shopping_list(self):
        ingredients = (
            Ingredient.objects.filter(recipes__in=self.recipes.all())
            .values('article_id')
            .annotate(quantity=Sum('quantity'))
            .annotate(weight=Sum('weight'))
        )
        for ingredient in ingredients:
            if ingredient.quantity:
                list = ShopList(shop=self)
                list.ingredients = ingredient
                list.save()
            elif ingredient.weight:
                list = ShopList(shop=self)
                list.ingredients = ingredient
                list.save()
        return 


class ShopList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ingredients = models.ForeignKey("Ingredient", null=True, on_delete=models.CASCADE)
    is_bought = models.BooleanField(default=False)
    bought_value = models.IntegerField(null=True)
    shop = models.OneToOneField("Shop", on_delete=models.CASCADE, null=True, related_name="ingredient_list")
    status = models.BooleanField(default=False)
