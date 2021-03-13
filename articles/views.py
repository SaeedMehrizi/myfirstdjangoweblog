from django.shortcuts import render
from . import models

# Create your views here.

def articles_list(request):
    articles = models.Articles.objects.all()
    args = {'articles':articles}
    return render(request, 'articles/articles_list.html', args)