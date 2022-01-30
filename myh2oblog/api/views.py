from django.shortcuts import render
from django.http import JsonResponse
from article.models import Articles, Tags, Categories
from django.views import View
from article.models import Articles, Tags, Categories


class PostArticleView(View):
    def get(self, request):
        categories = Categories.objects.all()
        tags = Tags.objects.all()
        return render(request, 'api/do_article.html', locals())


class EditArticleView(View):
    pass
