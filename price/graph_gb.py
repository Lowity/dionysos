from .gme_btc import get_bitcoin, get_gme
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
from plotly.offline import plot

def btc_graph():
    x_data, y_data = get_bitcoin()
    fig = go.Figure()
    scatter = go.Scatter(x=x_data, y=y_data, mode="lines", name="btc", opacity=0.9, marker_color="green")
    fig.update_layout(autosize=False, width=800, height=400,)
    fig.add_trace(scatter)
    plt_div_btc = plot(fig, output_type='div')
    return plt_div_btc

def gme_graph():
    x_data, y_data = get_gme()
    fig = go.Figure()
    scatter = go.Scatter(x=x_data, y=y_data, mode="lines", name="GME", opacity=0.9, marker_color="green")
    fig.update_layout(autosize=False, width=800, height=400)
    fig.add_trace(scatter)
    plt_div_gme = plot(fig, output_type="div")
    return plt_div_gme
