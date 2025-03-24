from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        """
        widgets = {
            'created_on' : forms.TextInput(
                attrs={
                    'type' :'datetime-local'
                }
            ),
            'updated_on' : forms.TextInput(
                attrs={
                    'type' :'datetime-local'
                }
            )
        } 
        """