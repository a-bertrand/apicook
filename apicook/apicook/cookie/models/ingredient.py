from django.db import models

"""
    Type gramme , litre qty .??? TODO choice field  

    unite_type
"""

class Ingredient(models.Model):
    QUANITTY = 'x'
    KG = 'kilogramme'
    G = 'gramme'
    L = 'litre'
    CL = 'centilitre'
    ML = 'millilitre'

    MEASURE_TYPE = (
        (QUANITTY, QUANITTY),
        (KG, KG),
        (G, G),
        (L, L),
        (CL, CL),
        (ML, ML)
    )

    value = models.IntegerField("Quantité", null=True, blank=True)
    measureType = models.CharField("Poids", choices=MEASURE_TYPE, null=True, blank=True)
    
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