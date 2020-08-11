from django.db import models
from .recipe import Recipe
from .ingredient import Ingredient
from .article import Article
from django.db.models import Sum
from itertools import chain


class ShoppingRecipeList (models.Model): 
    recipes = models.ManyToManyField(
        "Recipe",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    contributors = models.ManyToManyField(
        'auth.User', 
        related_name='shop', 
        blank=True
    )

    def __str__(self):
        return str(self.created_at)

    @staticmethod
    def generate_random_recipe(number_of_recipe = None, keeped_recipe_ids = []):
        if number_of_recipe == None:
            number_of_recipe = 1

        if keeped_recipe_ids != []:
           keeped_recipe = Recipe.objects.filter(id__in=keeped_recipe_ids).all()
           number_of_recipe = int(number_of_recipe) - len(list(keeped_recipe))
           return chain(Recipe.objects.order_by("?").exclude(id__in=keeped_recipe_ids)[:int(number_of_recipe)], keeped_recipe)

        return Recipe.objects.order_by("?").exclude(id__in=keeped_recipe_ids)[:int(number_of_recipe)]

    def _get_ordered_ingredients_from_reicpes_with_the_sum_of_their_quantity(self):
        return ( 
            Ingredient.objects.filter(recipes__in=self.recipes.all())
                .order_by('measure_type')
                .values('article_id', 'measure_type')
                .annotate(quantity=Sum('quantity')) 
        )

    def generate_shopping_list(self):
        ingredients = self._get_ordered_ingredients_from_reicpes_with_the_sum_of_their_quantity()
        for ingredient in ingredients:
            article = Article.objects.get(pk=ingredient['article_id'])
            new_list = ShoppingIngredientList(article=article, shop=self, measure_type=ingredient['measure_type'])
            new_list.total_quantity = ingredient['quantity']
            new_list.save()


class ShoppingIngredientList(models.Model):
    PARTIAL = 'PARTIAL'
    COMPLETE = 'COMPLETE'
    NOTTOUCH = 'NOTTOUCH'

    BOUGHT_TYPE = (
        (PARTIAL, PARTIAL),
        (COMPLETE, COMPLETE),
        (NOTTOUCH, NOTTOUCH),
    )

    article = models.ForeignKey("Article", null=True, on_delete=models.CASCADE, related_name="shop_list")
    bought_value = models.IntegerField(default=0)
    bought_status = models.CharField(default=NOTTOUCH, choices=BOUGHT_TYPE, max_length=10)
    measure_type = models.CharField("Type de mesure", choices=Ingredient.MEASURE_TYPE, max_length=20)
    shop = models.ForeignKey("ShoppingRecipeList", null=True, on_delete=models.CASCADE, related_name='list_content')
    total_quantity = models.IntegerField("Quantité", null=True, blank=True)


    def _update_bought_status(self):
        if (
            self.total_quantity is not None and 
            self.bought_status != self.COMPLETE and 
            self.bought_value == self.total_quantity
        ):
            self.bought_status = self.COMPLETE
        
        elif ( 
            self.bought_status != self.PARTIAL and 
            self.bought_value > 0 
        ):
            self.bought_status = self.PARTIAL 

        elif self.bought_status != self.NOTTOUCH and self.bought_value == 0:
            self.bought_status = self.NOTTOUCH

    def save(self, *args, **kwargs):
        self._update_bought_status()
        super(ShoppingIngredientList, self).save(*args, **kwargs)
