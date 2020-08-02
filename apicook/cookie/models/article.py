from django.db import models

class Article (models.Model): 
    name = models.CharField(max_length=30)
    how_many_found_in_recipes = models.IntegerField("Occurances", default=1)

    def __str__(self):
        return self.name
