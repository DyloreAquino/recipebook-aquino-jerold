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

def show_page(request, page : str):
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {
                        "name": "tomato",
                        "quantity": "3pcs"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "pork",
                        "quantity": "1kg"
                    },
                    {
                        "name": "water",
                        "quantity": "1L"
                    },
                    {
                        "name": "sinigang mix",
                        "quantity": "1 packet"
                    }
                ],
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {
                        "name": "garlic",
                        "quantity": "1 head"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "vinegar",
                        "quantity": "1/2cup"
                    },
                    {
                        "name": "water",
                        "quantity": "1 cup"
                    },
                    {
                        "name": "salt",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "whole black peppers",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kilo"
                    }
                ],
                "link": "/recipe/2"
            }
        ]
    }

    if page == "recipes_list":
        return render(request, "ledger/recipes_list.html", ctx)
    elif page == "recipe_1":
        return render(request, "ledger/recipe_1.html", ctx)
    elif page == "recipe_2":
        return render(request, "ledger/recipe_2.html", ctx)

