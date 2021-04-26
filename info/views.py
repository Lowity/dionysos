from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def about(request):
    #template = loader.get_template("info/about.html")
    return render(request, "info/about.html")

def correlation(request):
    #template = loader.get_template("info/correlation.html")
    return render(request, "info/correlation.html")