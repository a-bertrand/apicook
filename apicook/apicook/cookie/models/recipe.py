from django.db import models

class Recipe(models.Model):
    categories = models.ManyToManyField(
        "Category",
        blank=True,
    )
    title = models.CharField(max_length=30)
    text = models.CharField(
        'Description',
        max_length=1000, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name