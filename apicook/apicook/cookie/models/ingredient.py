from django.db import models

"""
    Type gramme , litre qty .??? TODO choice field  

    unite_type
"""

class Ingredient(models.Model):
    quantity = models.IntegerField("Quantité", null=True, blank=True)
    weight = models.IntegerField("Poids", null=True, blank=True)
    
    article = models.ForeignKey(
        "Article", 
        related_name=("ingredients"), 
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