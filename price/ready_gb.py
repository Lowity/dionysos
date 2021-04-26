from .gme_btc import get_bitcoin, get_gme
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
from plotly.offline import plot
import numpy as np

def btc_data():
    x_data_btc, y_data_btc = get_bitcoin()
    return x_data_btc, y_data_btc

def gme_data():
    x_data_gme, y_data_gme = get_gme()
    return x_data_gme, y_data_gme

def btc_graph():
    x_data_btc, y_data_btc = btc_data()
    fig = go.Figure()
    scatter = go.Scatter(x=x_data_btc, y=y_data_btc, mode="lines", name="btc", opacity=0.9, marker_color="green")
    fig.update_layout(autosize=False, width=800, height=400,)
    fig.add_trace(scatter)
    plt_div_btc = plot(fig, output_type='div', config=dict(displayModeBar=False))
    return plt_div_btc

def gme_graph():
    x_data_gme, y_data_gme = gme_data()
    fig = go.Figure()
    scatter = go.Scatter(x=x_data_gme, y=y_data_gme, mode="lines", name="GME", opacity=0.9, marker_color="green")
    fig.update_layout(autosize=False, width=800, height=400)
    fig.add_trace(scatter)
    plt_div_gme = plot(fig, output_type="div", config=dict(displayModeBar=False))
    return plt_div_gme

def corr():
    x_data_gme, y_data_gme = gme_data()
    x_data_btc, y_data_btc = btc_data()

    corr = np.corrcoef(y_data_gme, y_data_btc)[0, 1] * 100
    return corr


