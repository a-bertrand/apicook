from django.db import models

"""
    Type gramme , litre qty .??? TODO choice field  

    unite_type
"""

class Ingredient(models.Model):
    QUANTITY = 'x'
    MG = 'Milligramme'
    KG = 'Kilogramme'
    G = 'Gramme'
    L = 'Litre'
    CL = 'Centilitre'
    ML = 'Millilitre'
    CC = 'Cuillère à café'
    CS = 'Cuillère à soupe'
    GOU = 'GOUSSE'

    MEASURE_TYPE = (
        (QUANTITY, QUANTITY),
        (MG,MG),
        (KG, KG),
        (G, G),
        (L, L),
        (CL, CL),
        (ML, ML),
        (CC, CC),
        (CS, CS),
        (GOU,GOU)
    )

    quantity = models.IntegerField("Quantité")
    measure_type = models.CharField("Type de mesure", choices=MEASURE_TYPE, max_length=20)
    
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
