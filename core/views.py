from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def historias(request):
    return render(request, 'historias.html')

def novidades(request):
    return render(request, 'novidades.html')