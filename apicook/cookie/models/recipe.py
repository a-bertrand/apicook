from django.db import models
from django.utils.html import mark_safe


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
    image = models.FileField(upload_to='recipes/', null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='recipes', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title
    
    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(f'<img src="{self.image.url}" />')

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name