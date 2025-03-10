from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient


class RecipeIngredientInline(admin.TabularInline):
    """Create RecipeIngredient inline for RecipeAdmin."""

    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    """Create admin panel for Recipe."""

    inlines = [RecipeIngredientInline,]


class IngredientAdmin(admin.ModelAdmin):
    """Create Ingredient admin panel."""

    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
