from django.urls import path

from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('correlation', views.correlation, name='correlation')
]
