from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
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
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recipe'] = Recipe.objects.get(pk=self.kwargs['pk'])
        return ctx

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
            recipe_image.save()
            return redirect(self.get_success_url())
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
    
    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})


