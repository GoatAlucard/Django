from django.shortcuts import render,HttpResponse

# Create your views here.

def contacto(request):
    return render(request, "core/contacto.html")

def index(request):
    return render(request, "core/index.html")

def acerca(request):
    return render(request, "core/acerca.html")




