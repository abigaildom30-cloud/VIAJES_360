from django.db.models import Q
from django.shortcuts import render
from .models import Destino


def inicio(request):
    destinos = Destino.objects.filter(destacado=True)[:6]

    if destinos.count() == 0:
        destinos = Destino.objects.all()[:6]

    return render(request, "viajes/inicio.html", {"destinos": destinos})


def destinos(request):
    lista = Destino.objects.all()

    busqueda = request.GET.get("buscar", "").strip()
    pais = request.GET.get("pais", "").strip()

    if busqueda:
        lista = lista.filter(
            Q(nombre__icontains=busqueda)
            | Q(ciudad__icontains=busqueda)
            | Q(pais__icontains=busqueda)
            | Q(descripcion__icontains=busqueda)
        )

    if pais:
        lista = lista.filter(pais__iexact=pais)

    paises = (
        Destino.objects.exclude(pais="")
        .values_list("pais", flat=True)
        .distinct()
        .order_by("pais")
    )

    return render(
        request,
        "viajes/destinos.html",
        {
            "destinos": lista,
            "paises": paises,
            "busqueda": busqueda,
            "pais_seleccionado": pais,
        },
    )


def nosotros(request):
    return render(request, "viajes/nosotros.html")


def servicios(request):
    return render(request, "viajes/servicios.html")


def contacto(request):
    return render(request, "viajes/contacto.html")
