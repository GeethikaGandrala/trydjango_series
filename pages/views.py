from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello user..!Welcome to django</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4242, 12313,"MaGee"]
    }
    return render(request, "about.html", my_context)
