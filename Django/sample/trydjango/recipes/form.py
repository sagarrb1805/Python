from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    error_css_class = "error-field"
    required_css_class = "required-field"
    # name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 'placeholder':"name"}))
    name = forms.CharField(help_text="This is your help text for name field. <a href=''> Contact Us </a>")
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                'placeholder':f"Recipe {str(field)}",
                'class':'form-control'
            }
            self.fields[str(field)].widget.attrs.update(new_data)
            # self.fields[str(field)].widget.attrs.update(placeholder=f"Recipe {str(field)}",)
        # self.fields['name'].label = ''
        # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['description'].widget.attrs.update({'rows':2})
        self.fields['directions'].widget.attrs.update({'rows':4})

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
