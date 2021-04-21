from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .graph_gb import btc_graph, gme_graph


# Create your views here.
def index(request):
    template = loader.get_template("price/index.html")
    return render(request, "price/index.html")

def btc_site(request):
    return render(request, "price/graph_btc.html", context={'plot_div': plt_div_btc})

def gme_site(request):
    return render(request, "price/graph_gme.html", context={'plot_div': plt_div_gme})

plt_div_gme = gme_graph()
plt_div_btc = btc_graph()