from django.db import models
from django.urls import reverse
from accounts.models import User

class Ingredient(models.Model):
    """A model for ingredients, storing their name."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of the Ingredient."""
        return str(self.name)

    def get_absolute_url(self):
        """Return the URL associated with the Ingredient."""
        return reverse('ledger:ingredient_detail', args=[str(self.pk)])


class Recipe(models.Model):
    """A model for recipes, storing their name."""

    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the Recipe."""
        return str(self.name)

    def get_absolute_url(self):
        """Return the URL associated with the Recipe."""
        return reverse('ledger:recipe_detail', args=[str(self.pk)])


class RecipeImage(models.Model):
    """A model for the image of a recipe."""

    image = models.ImageField(blank=False, upload_to='images/')
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='recipe_image'
    )


class RecipeIngredient(models.Model):
    """An associative entity between recipes and ingredients."""

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