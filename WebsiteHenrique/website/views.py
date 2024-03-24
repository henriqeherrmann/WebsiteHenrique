from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "website/home.html")

def sobrePessoal(request):
    return render(request, "website/sobrePessoal.html")

def sobreProfissional(request):
    return render(request, "website/sobreProfissional.html")

def contato(request):
    return render(request, "website/contato.html")