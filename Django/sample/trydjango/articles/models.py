from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.db.models import Q
from .utils import slugify_instance_title
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class ModelManager(models.Manager):
    def search(self, query=None):
        if query is None or '':
            return self.get_queryset().none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.get_queryset().filter(lookups)

class Article(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False
            , null=True, blank=True)

    objects = ModelManager()

    def get_absolute_url(self):
        return reverse('articles:article', kwargs={"slug": self.slug})

    # def save(self, *args, **kwargs):
    #     #set something 
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    #     #do another something



def article_pre_save(sender, instance, *args, **kwargs):
    print('pre save')
    if instance.slug is None:
        slugify_instance_title(instance)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    print('post save')
    if created:
         slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)