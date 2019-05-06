# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models



class Article (models.Model): 
    name = models.CharField(max_length=30)
    ingredients = models.ForeignKey(
        "Ingredient", 
        related_name=("article"), 
        on_delete=models.CASCADE, 
        null=True
    )
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    quantity = models.IntegerField("Quantité")
    weight = models.IntegerField("Poids")

    def __str__(self):
        return self.article.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(
        max_length=1000, 
        blank=True, 
        null=True
    )
    ingredients = models.ForeignKey(
        "Recipe", 
        verbose_name=("Ingredient"), 
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return self.title