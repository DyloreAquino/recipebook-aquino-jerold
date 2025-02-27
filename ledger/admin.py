from django.contrib import admin
from .models import Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    """Create RecipeIngredient inline for RecipeAdmin."""

    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    """Create admin panel for Recipe."""

    inlines = [RecipeIngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
