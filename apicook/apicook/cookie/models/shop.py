from django.db import models
from .recipe import Recipe


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

"""
    def generate_shop_list():
        for recipe in self.recipes:
            for ingredient in recipe.ingredrients:
                # pour chaque ingredient d'un même article les liés par poids ou quantité
                select * from ingredient group by article having weight > 0 
                select * from ingredient group by article having quantity > 0 

                Ingredient.filter(recipe_set=self).order_by(article)
"""

class ShopList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField("Ingredient")
    Shop = models.OneToOneField("Shop", on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
