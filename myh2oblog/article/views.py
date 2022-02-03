from django.shortcuts import render, HttpResponse, reverse, redirect
from .models import Articles
from django.core.paginator import Paginator


def index(request):
    articles = Articles.objects.all().order_by("-created")
    articles = Paginator(articles, 4)
    page = request.GET.get('page')
    articles = articles.get_page(page)
    return render(request, "article/index.html", locals())


def article_detail(request, nid):
    article = Articles.objects.get(id=nid)
    return render(request, 'article/article_detail.html', locals())
