from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm, PerfilForm, InmuebleForm

from django.contrib.auth.decorators import login_required
from .models import PerfilUsuario, Inmueble, Region, Comuna


def registro(request):

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegistroForm()

    return render(
        request,
        "registration/registro.html",
        {"form": form}
    )

@login_required
def perfil(request):
    perfil_usuario = PerfilUsuario.objects.get(
        usuario=request.user
    )

    return render(
        request,
        "perfil.html",
        {
            "perfil": perfil_usuario
        }
    )

@login_required
def editar_perfil(request):

    perfil_usuario = PerfilUsuario.objects.get(
        usuario=request.user
    )

    if request.method == "POST":
        form = PerfilForm(
            request.POST,
            instance=perfil_usuario
        )

        if form.is_valid():
            form.save()
            return redirect("perfil")

    else:
        form = PerfilForm(
            instance=perfil_usuario
        )

    return render(
        request,
        "editar_perfil.html",
        {
            "form": form
        }
    )

@login_required
def agregar_inmueble(request):

    perfil_usuario = PerfilUsuario.objects.get(
        usuario=request.user
    )

    if perfil_usuario.tipo_usuario != "arrendador":
        return redirect("perfil")

    if request.method == "POST":
        form = InmuebleForm(request.POST)

        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user
            inmueble.save()

            return redirect("perfil")

    else:
        form = InmuebleForm()

    return render(
        request,
        "agregar_inmueble.html",
        {
            "form": form
        }
    )

@login_required
def mis_inmuebles(request):

    perfil_usuario = PerfilUsuario.objects.get(
        usuario=request.user
    )

    if perfil_usuario.tipo_usuario != "arrendador":
        return redirect("perfil")

    inmuebles = Inmueble.objects.filter(
        arrendador=request.user
    )

    return render(
        request,
        "mis_inmuebles.html",
        {
            "inmuebles": inmuebles
        }
    )

@login_required
def editar_inmueble(request, inmueble_id):

    perfil_usuario = PerfilUsuario.objects.get(
        usuario=request.user
    )

    if perfil_usuario.tipo_usuario != "arrendador":
        return redirect("perfil")

    inmueble = Inmueble.objects.get(
        id=inmueble_id,
        arrendador=request.user
    )

    if request.method == "POST":
        form = InmuebleForm(
            request.POST,
            instance=inmueble
        )

        if form.is_valid():
            form.save()
            return redirect("mis_inmuebles")

    else:
        form = InmuebleForm(
            instance=inmueble
        )

    return render(
        request,
        "editar_inmueble.html",
        {
            "form": form,
            "inmueble": inmueble
        }
    )

@login_required
def eliminar_inmueble(request, inmueble_id):
    perfil_usuario = PerfilUsuario.objects.get(usuario=request.user)

    if perfil_usuario.tipo_usuario != "arrendador":
        return redirect("perfil")

    inmueble = Inmueble.objects.get(
        id=inmueble_id,
        arrendador=request.user
    )

    return render(
        request,
        "eliminar_inmueble.html",
        {"inmueble": inmueble}
    )

@login_required
def confirmar_eliminar_inmueble(request, inmueble_id):
    perfil_usuario = PerfilUsuario.objects.get(usuario=request.user)

    if perfil_usuario.tipo_usuario != "arrendador":
        return redirect("perfil")

    inmueble = Inmueble.objects.get(
        id=inmueble_id,
        arrendador=request.user
    )

    if request.method == "POST":
        inmueble.delete()
        return redirect("mis_inmuebles")

    return redirect("mis_inmuebles")

@login_required
def oferta_inmuebles(request):
    perfil_usuario = PerfilUsuario.objects.get(usuario=request.user)

    if perfil_usuario.tipo_usuario != "arrendatario":
        return redirect("perfil")

    inmuebles = Inmueble.objects.all()

    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    region_seleccionada = request.GET.get("region", "")
    comuna_seleccionada = request.GET.get("comuna", "")

    if region_seleccionada:
        inmuebles = inmuebles.filter(
            comuna__region_id=region_seleccionada
        )

    if comuna_seleccionada:
        inmuebles = inmuebles.filter(
            comuna_id=comuna_seleccionada
        )

    return render(
        request,
        "oferta_inmuebles.html",
        {
            "inmuebles": inmuebles,
            "regiones": regiones,
            "comunas": comunas,
            "region_seleccionada": region_seleccionada,
            "comuna_seleccionada": comuna_seleccionada,
        }
    )