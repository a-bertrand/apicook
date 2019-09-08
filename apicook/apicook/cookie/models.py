# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Article (models.Model): 
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    quantity = models.IntegerField("Quantité", null=True, blank=True)
    weight = models.IntegerField("Poids", null=True, blank=True)
    article = models.ForeignKey(
        "Article", 
        related_name=("article"), 
        on_delete=models.CASCADE
    )
    recipes = models.ForeignKey(
        "Recipe", 
        verbose_name=("Recette"), 
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    def __str__(self):
        return self.article.name

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

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
        