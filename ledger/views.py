from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    """A ListView for the Recipe model."""

    model = Recipe
    template_name = 'ledger/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    """A DetailView for the Recipe model."""

    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    redirect_field_name = '/recipes/list'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    """A CreateView for creating Recipes."""

    model = Recipe
    template_name = 'ledger/recipe_add.html'

    form_class = RecipeForm


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    """A CreateView for adding Images to Recipes"""

    model = RecipeImage
    template_name = 'ledger/recipe_add_image.html'

    form_class = RecipeImageForm