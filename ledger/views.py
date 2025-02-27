from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'