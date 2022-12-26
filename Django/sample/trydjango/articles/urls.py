
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.article_search_view, name="article_search_view"),
    path("create/", views.article_create_view, name="aticle_create_view"),
    path("<slug:slug>/", views.article_view, name='article'),
]
