from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# This is a global..
tasks = []

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "bankjobbd/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("bankjobbd:index")) 
        else:
            return render(request, "bankjobbd/add.html", {
                "form": form
            })
    return render(request, "bankjobbd/add.html", {
        "form": NewTaskForm()
    })
