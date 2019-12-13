from django.db import models
from .recipe import Recipe


class Step(models.Model):
    number = models.IntegerField("Numéro d'étape")
    text = models.CharField("Détail", max_length=50)
    
    recipe = models.ForeignKey(
        "Recipe", 
        verbose_name=("Recette"), 
        on_delete=models.CASCADE,
        related_name='steps'
    )

    def __str__(self):
        return str(self.number) + ' - '+ self.text
