from django.urls import path
from . import views

urlpatterns = [
    path('juegos/', views.juegos_list, name='juegos_list'),
    path('plataformas/', views.plataformas_list, name='plataformas_list'),
    path('desarrolladoras/', views.desarrolladoras_list, name='desarrolladoras_list'),
]
