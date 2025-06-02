from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def show_get(request):
    id = request.GET.get("id")
    return render(request, "show_get.html", {"id":id})


def form_get(request):
    return render(request, "form_get.html")


def submit_form_get(request):
    name = request.GET.get("name")
    return HttpResponse(f"<h1> AHOJ, {name}</h1>")


def form_post(request):
    if request.method == "POST":
        name = request.POST.get("name")

        return HttpResponse(f"<h1> AHOJ, {name}</h1>")

    return render(request, "form_post.html")