from django.db import models
from .recipe import Recipe
from .ingredient import Ingredient
from .article import Article
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
            new_list = ShopList(article=article, shop=self, measure_type=ingredient['measure_type'])
            new_list.total_quantity = ingredient['quantity']
            new_list.save()


class ShopList(models.Model):
    PARTIAL = 'PARTIAL'
    COMPLETE = 'COMPLETE'
    NOTTOUCH = 'NOTTOUCH'

    BOUGHT_TYPE = (
        (PARTIAL, PARTIAL),
        (COMPLETE, COMPLETE),
        (NOTTOUCH, COMPLETE),
    )

    article = models.ForeignKey("Article", null=True, on_delete=models.CASCADE, related_name="shop_list")
    bought_value = models.IntegerField(default=0)
    shop = models.ForeignKey("Shop", null=True, on_delete=models.CASCADE, related_name='list_content')

    created_at = models.DateTimeField(auto_now_add=True)
    
    bought_status = models.CharField(default=NOTTOUCH, choices=BOUGHT_TYPE, max_length=10)

    total_quantity = models.IntegerField("Quantité", null=True, blank=True)
    measure_type = models.CharField("Type de mesure", choices=Ingredient.MEASURE_TYPE, max_length=20)

    updated_at = models.DateTimeField(auto_now=True)

    def update_bought_status(self):
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
        self.update_bought_status()
        super(ShopList, self).save(*args, **kwargs)
