from django.shortcuts import render, HttpResponse, reverse, redirect


def index(request):
    return render(request, "article/index.html", locals())
