from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    """Create RecipeIngredient inline for RecipeAdmin."""

    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    """Create admin panel for Recipe."""

    model = Recipe
    inlines = [RecipeIngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
