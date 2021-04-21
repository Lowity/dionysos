from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("btc", views.btc_site, name="btc"),
    path("gme", views.gme_site, name="gme")
]