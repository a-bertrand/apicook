# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models



class Article (models.Model): 
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    article = models.OneToOneField("Article", verbose_name=("article"), on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantité")
    weight = models.IntegerField("Poids")

    def __str__(self):
        return self.article.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=1000, blank=True, null=True)
    ingredient = models.ManyToManyField("Ingredient", verbose_name=("Ingredient"), blank=True)

    def __str__(self):
        return self.article.title