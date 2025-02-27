from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='recipe')
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='ingredients')