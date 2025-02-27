from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail')
]

# This might be needed, depending on your Django version
app_name = "ledger"