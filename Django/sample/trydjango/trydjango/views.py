import random
from django.http import HttpResponse
from articles.models import Article
from django.shortcuts import render



def home_view(request):
    num = random.randint(1, 3)
    article = Article.objects.get(id=num)
    article_list = Article.objects.all()
    print(num)
    num_list = [1, 2, 3]
    context = {"title":article.title, "content":article.content,'id':article.id, 'num_list':num_list, 'article_list':article_list}
    return render(request, "home.html", context)


