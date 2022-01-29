from django.shortcuts import render, HttpResponse, reverse, redirect
from .models import Articles


def index(request):
    articles = Articles.objects.all().order_by("-created")
    return render(request, "article/index.html", locals())


def article_detail(request, nid):
    article = Articles.objects.get(id=nid)
    return render(request, 'article/article_detail.html', locals())
