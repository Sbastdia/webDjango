from django.http import HttpRequest
from django.shortcuts import render

def portfolio(request):
    return render(
        request,
        "portfolio.html",
        
    )

def home(request):
    return render(
        request,
        "home.html",
        
    )


def about(request):
    return render(
        request,
        "about.html",
        
    )


def contact(request):
    return render(
        request,
        "contact.html",
        
    )

