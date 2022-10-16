from django.shortcuts import render
from django.shortcuts import render
from familia.models import Familiar

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "familia/familiares.html", {"lista_familiares": lista_familiares})
