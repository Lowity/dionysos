from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .ready_gb import btc_graph, gme_graph, corr


# Create your views here.
def index(request):
    template = loader.get_template("price/index.html")
    return render(request, "price/index.html", context={'plot_div_gme': plt_div_gme, 'plot_div_btc':plt_div_btc, 'corr':corr})

plt_div_gme = gme_graph()
plt_div_btc = btc_graph()
corr = corr()