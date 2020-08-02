from django.db import models
from .ingredient import Ingredient


class MatchKeywords(models.Model):
    keywords = models.CharField(max_length=300)
    measure_type = models.CharField("Type de mesure", choices=Ingredient.MEASURE_TYPE, max_length=20)
    order = models.IntegerField("Ordre de recherche", default=99)
