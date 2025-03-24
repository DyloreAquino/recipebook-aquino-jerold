from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    """Create RecipeIngredient inline for RecipeAdmin."""

    model = RecipeIngredient
    extra = 1


class RecipeImageInline(admin.TabularInline):
    """Create RecipeImage inline for RecipeAdmin."""

    model = RecipeImage
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    """Create admin panel for Recipe."""

    inlines = [RecipeIngredientInline, RecipeImageInline,]


class IngredientAdmin(admin.ModelAdmin):
    """Create Ingredient admin panel."""

    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
