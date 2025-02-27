from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe


class RecipeListView(ListView):
    """A ListView for the Recipe model."""

    model = Recipe
    template_name = 'ledger/recipes_list.html'


class RecipeDetailView(DetailView):
    """A DetailView for the Recipe model."""

    model = Recipe
    template_name = 'ledger/recipe_detail.html'