from django.db import models
from django.utils.html import mark_safe
from django.db.models.aggregates import Count
from random import randint

class Recipe(models.Model):
    categories = models.ManyToManyField(
        "Category",
        blank=True,
    )
    title = models.CharField(max_length=30)
    text = models.CharField(
        'Description',
        max_length=1000, 
        blank=True, 
        null=True
    )
    image = models.FileField(upload_to='recipes/', null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='recipes', on_delete=models.CASCADE, null=True, blank=True)
    how_many = models.IntegerField(null=True)


    def __str__(self):
        return self.title
    
    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(f'<img src="{self.image.url}" />')

    @classmethod
    def get_random_recipe(self):
        count = Recipe.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return Recipe.objects.all()[random_index]


class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name