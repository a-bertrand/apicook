# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Ingredient, Recipe, Category, Step

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Step)
class StepsAdmin(admin.ModelAdmin):
    pass


class IngredientInline(admin.TabularInline):
    model = Ingredient

class StepsInline(admin.TabularInline):
    model = Step

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
        StepsInline
    ]
    fields = ( 'image_tag', )
    readonly_fields = ('image_tag',)