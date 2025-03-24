from django import forms
from .models import Recipe, RecipeImage


class RecipeForm(forms.ModelForm):
    """A class for creating recipes through a form."""

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeImageForm(forms.ModelForm):
    """A class for adding images to recipes through a form."""

    class Meta:
        model = RecipeImage
        fields = '__all__'
