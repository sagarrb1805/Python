from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.http import HttpResponse, Http404
from django.urls import reverse

from .models import Recipe, RecipeIngredient
from .form import RecipeForm, RecipeIngredientForm

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        'object_list':qs
    }
    return render(request, "recipes/list.html", context)

@login_required
def recipe_detail_view(request,id=None):
    # obj = get_object_or_404(Recipe, id=id, user=request.user)  
    hx_url = reverse("recipes:hx-detail", kwargs={"id": id})

    context = {
        'hx_url':hx_url
    }
    return render(request, 'recipes/detail.html', context)



@login_required
def recipe_detail_hx_view(request,id=None):
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        # raise Http404
        return HttpResponse('Not found')
    # obj = get_object_or_404(Recipe, id=id, user=request.user)  
    context = {
        'obj':obj
    }
    return render(request, 'recipes/partials/detail.html', context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)

@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    # form_2 = RecipeIngredientForm(request.POST or None)

    # Formset = modelformset_factory(Model, form=ModelForm, extra=0)
    RecipeIngredientFormset = modelformset_factory(RecipeIngredient, 
                            form=RecipeIngredientForm, extra=0)
    qs = obj.recipeingredient_set.all()
    formset = RecipeIngredientFormset(request.POST or None, queryset=qs)

    
    context = {
        'form':form,
        'formset':formset,
        'object':obj
    }
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            child.recipe = parent
            child.save()
        # child = form_2.save(commit=False)
        # child.recipe = parent
        # child.save()
        context['message'] = "updated succesfully"
    if request.htmx:
        return render(request, "recipes/partials/form.html", context)
    return render(request, "recipes/create-update.html", context)
