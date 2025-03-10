from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe


class RecipeListView(ListView):
    """A ListView for the Recipe model."""

    model = Recipe
    template_name = 'ledger/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    """A DetailView for the Recipe model."""

    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    redirect_field_name = '/recipes/list'