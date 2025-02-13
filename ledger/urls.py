from django.urls import path
from .views import show_page

urlpatterns = [
    path('recipes/list', show_page, kwargs={"page" : "recipes_list"}, name='recipes_list'),
    path('recipe/1', show_page, kwargs={"page" : "recipe_1"}, name='recipe_1'),
    path('recipe/2', show_page, kwargs={"page" : "recipe_2"}, name='recipe_2'),
]

# This might be needed, depending on your Django version
app_name = "ledger"