from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('sobrePessoal/', views.sobrePessoal, name="sobrePessoal"),
    path('sobreProfissional/', views.sobreProfissional, name="sobreProfissional"),
    path('contato/', views.contato, name="contato")

]