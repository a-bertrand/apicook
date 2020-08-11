# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
        Article, Ingredient, 
        Recipe, Category, Step, 
        ShoppingRecipeList, MatchKeywords, 
        ShoppingIngredientList
    )
from import_export.admin import ImportExportModelAdmin

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','how_many_found_in_recipes',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Step)
class StepsAdmin(admin.ModelAdmin):
    pass

class ShoppingIngredientListInline(admin.TabularInline):
    model = ShoppingIngredientList

@admin.register(ShoppingRecipeList)
class ShoppingRecipeListAdmin(admin.ModelAdmin):
    inlines = [
        ShoppingIngredientListInline,
    ]


@admin.register(MatchKeywords)
class StepsInline(ImportExportModelAdmin):
    list_display = ('measure_type', 'order')
    model = MatchKeywords
    ordering = ('order',)

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
    fields = ( 'image_tag', 'categories', 'title', 'text', 'image', 'owner')
    readonly_fields = ('image_tag',)