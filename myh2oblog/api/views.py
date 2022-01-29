from django.shortcuts import render
from django.http import JsonResponse
from article.models import Articles, Tags, Categories
from django.views import View


class PostArticleView(View):
    def get(self, request):
        return render(request, 'api/do_article.html')


class EditArticleView(View):
    pass
