from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "webdrive/index.html")

# def greet(request, name):
#     return HttpResponse(f"Hello {name}")

def greet(request, name):
    return render(request, "webdrive/greet.html",{
        "name":name.capitalize()
    })
