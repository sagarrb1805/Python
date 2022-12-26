from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
# Create your views here.

def article_search_view(request):
    query = request.GET.get("q")
    qs = Article.objects.search(query=query)
    context = {'object_list': qs}
    return render(request, "search.html",context = context)

@login_required
def article_create_view(request):

    form = ArticleForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        return redirect(article_object.get_absolute_url())
        # context["object"] = article_object
        # context["created"] = True

        #article.save()
    
    return render (request, "create.html", context)

def article_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except:
            raise Http404
        context = {
            'object':article_obj
        }
    return render(request, "article.html", context)