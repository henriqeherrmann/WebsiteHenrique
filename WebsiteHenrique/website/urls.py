from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('sobrePessoal/', views.sobrePessoal),
    path('sobreProfissional/', views.sobreProfissional),
    path('contato/', views.contato)

]