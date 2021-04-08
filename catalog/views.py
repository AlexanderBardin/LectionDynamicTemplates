from django.shortcuts import render
from datetime import datetime


def new_view(request):
    context = {"datetime": datetime.now()}

    return render(request, "catalog/home.html", context)


def detail(request):
    return render(request, "catalog/detail.html")
