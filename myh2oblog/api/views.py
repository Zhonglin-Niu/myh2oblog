from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from article.models import Articles, Tags, Categories


class PostArticleView(View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('/')
        categories = Categories.objects.all()
        tags = Tags.objects.all()
        return render(request, 'api/do_article.html', locals())

    def post(self, request):
        data = request.data
        print(data)
        msg = {
            "code": 425,
            "msg": "有信息未填或者不正确，请检查",
            "id": "",
        }
        for item in data:
            if data[item] in ['', []]:
                return JsonResponse(msg)
        category = Categories.objects.get(id=data["category"])
        article = Articles.objects.create(title=data["title"], category=category, description=data["description"],
                                          content=data["content"], cover=data["cover"])
        for tag in data["tag"]:
            article.tag.add(tag)
        msg["code"] = 0
        msg["msg"] = "发布成功，即将跳转……"
        msg["id"] = article.id
        return JsonResponse(msg)


class EditArticleView(View):
    def get(self, request, nid):
        if not request.user.is_superuser:
            return redirect('/')
        categories = Categories.objects.all()
        tags = Tags.objects.all()
        article = Articles.objects.filter(id=nid)
        if not article:
            return redirect('/')
        article = article.first()
        tagss = [str(tag.id) for tag in article.tag.all()]
        print(tagss)
        return render(request, 'api/edit_article.html', locals())

    def post(self, request, nid):
        data = request.data
        print(data)
        msg = {
            "code": 425,
            "msg": "有信息未填或者不正确，请检查",
            "id": "",
        }
        for item in data:
            if data[item] in ['', []]:
                return JsonResponse(msg)
        category = Categories.objects.get(id=data["category"])
        article = Articles.objects.filter(id=nid)
        if not article:
            return redirect('/')
        article.update(title=data["title"], category=category, description=data["description"],
                       content=data["content"], cover=data["cover"])
        article.first().tag.clear()
        for tag in data["tag"]:
            article.first().tag.add(tag)
        msg["code"] = 0
        msg["msg"] = "修改成功，即将跳转……"
        msg["id"] = article.first().id
        return JsonResponse(msg)
