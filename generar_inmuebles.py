import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arriendo.settings")
django.setup()

from inmuebles.models import Inmueble, Comuna, TipoInmueble


# Comunas que utilizaremos en los ejemplos
comunas_nombres = [
    "Arica",
    "Valparaíso",
    "Viña del Mar",
    "Santiago",
    "Concepción",
    "Puerto Montt",
]

# Buscar las comunas en la base de datos
comunas = {}

for nombre in comunas_nombres:
    comuna = Comuna.objects.filter(nombre=nombre).first()

    if not comuna:
        raise ValueError(
            f"No se encontró la comuna '{nombre}' en la base de datos."
        )

    comunas[nombre] = comuna


# Buscar los tipos de inmueble
tipos = {}

for nombre in [
    "Casa",
    "Departamento",
    "Cabaña",
    "Parcela",
    "Local comercial",
]:
    tipo = TipoInmueble.objects.filter(nombre=nombre).first()

    if not tipo:
        raise ValueError(
            f"No se encontró el tipo de inmueble '{nombre}'."
        )

    tipos[nombre] = tipo


# Datos de los inmuebles
inmuebles = [
    {
        "nombre": "Casa familiar en Arica",
        "descripcion": "Casa amplia y luminosa ideal para una familia.",
        "m2_construidos": 95.0,
        "m2_totales": 180.0,
        "estacionamientos": 2,
        "habitaciones": 3,
        "banos": 2,
        "direccion": "Av. Principal 120",
        "comuna": "Arica",
        "tipo": "Casa",
        "precio_mensual": "650000.00",
    },
    {
        "nombre": "Departamento centro de Valparaíso",
        "descripcion": "Departamento cercano a servicios y transporte.",
        "m2_construidos": 65.0,
        "m2_totales": 65.0,
        "estacionamientos": 1,
        "habitaciones": 2,
        "banos": 1,
        "direccion": "Calle Independencia 450",
        "comuna": "Valparaíso",
        "tipo": "Departamento",
        "precio_mensual": "550000.00",
    },
    {
        "nombre": "Casa en Viña del Mar",
        "descripcion": "Casa cómoda ubicada en sector residencial.",
        "m2_construidos": 110.0,
        "m2_totales": 200.0,
        "estacionamientos": 2,
        "habitaciones": 4,
        "banos": 2,
        "direccion": "Calle Los Aromos 321",
        "comuna": "Viña del Mar",
        "tipo": "Casa",
        "precio_mensual": "850000.00",
    },
    {
        "nombre": "Departamento en Santiago",
        "descripcion": "Departamento moderno cercano al metro.",
        "m2_construidos": 55.0,
        "m2_totales": 55.0,
        "estacionamientos": 1,
        "habitaciones": 2,
        "banos": 1,
        "direccion": "Av. Portugal 850",
        "comuna": "Santiago",
        "tipo": "Departamento",
        "precio_mensual": "600000.00",
    },
    {
        "nombre": "Casa familiar en Santiago",
        "descripcion": "Casa con patio y espacios para toda la familia.",
        "m2_construidos": 120.0,
        "m2_totales": 250.0,
        "estacionamientos": 2,
        "habitaciones": 4,
        "banos": 3,
        "direccion": "Pasaje Los Robles 145",
        "comuna": "Santiago",
        "tipo": "Casa",
        "precio_mensual": "950000.00",
    },
    {
        "nombre": "Departamento en Concepción",
        "descripcion": "Departamento cercano a universidades y comercio.",
        "m2_construidos": 60.0,
        "m2_totales": 60.0,
        "estacionamientos": 1,
        "habitaciones": 2,
        "banos": 1,
        "direccion": "Av. Los Carrera 620",
        "comuna": "Concepción",
        "tipo": "Departamento",
        "precio_mensual": "580000.00",
    },
    {
        "nombre": "Cabaña en Puerto Montt",
        "descripcion": "Cabaña acogedora en un entorno tranquilo.",
        "m2_construidos": 70.0,
        "m2_totales": 150.0,
        "estacionamientos": 2,
        "habitaciones": 3,
        "banos": 1,
        "direccion": "Camino Austral 900",
        "comuna": "Puerto Montt",
        "tipo": "Cabaña",
        "precio_mensual": "700000.00",
    },
    {
        "nombre": "Parcela en Puerto Montt",
        "descripcion": "Parcela amplia ideal para vivir y disfrutar de la naturaleza.",
        "m2_construidos": 100.0,
        "m2_totales": 5000.0,
        "estacionamientos": 4,
        "habitaciones": 3,
        "banos": 2,
        "direccion": "Ruta 5 Sur km 1020",
        "comuna": "Puerto Montt",
        "tipo": "Parcela",
        "precio_mensual": "900000.00",
    },
]


fixture = []

for pk, inmueble in enumerate(inmuebles, start=1):
    fixture.append({
        "model": "inmuebles.inmueble",
        "pk": pk,
        "fields": {
            "nombre": inmueble["nombre"],
            "descripcion": inmueble["descripcion"],
            "m2_construidos": inmueble["m2_construidos"],
            "m2_totales": inmueble["m2_totales"],
            "estacionamientos": inmueble["estacionamientos"],
            "habitaciones": inmueble["habitaciones"],
            "banos": inmueble["banos"],
            "direccion": inmueble["direccion"],
            "comuna": comunas[inmueble["comuna"]].id,
            "tipo_inmueble": tipos[inmueble["tipo"]].id,
            "precio_mensual": inmueble["precio_mensual"],
        },
    })


with open(
    "inmuebles/fixtures/inmuebles.json",
    "w",
    encoding="utf-8"
) as archivo:
    json.dump(
        fixture,
        archivo,
        ensure_ascii=False,
        indent=4
    )


print("Fixture de inmuebles generado correctamente.")
print(f"Inmuebles generados: {len(fixture)}")
print("Archivo: inmuebles/fixtures/inmuebles.json")