import json

# Archivo de origen
archivo_origen = "comunas-origen.json"

# Archivo que utilizará Django
archivo_destino = "inmuebles/fixtures/comunas.json"


# Relación entre los nombres del archivo de origen
# y los ID de las regiones que ya cargamos en Django.
region_ids = {
    "Arica y Parinacota": 1,
    "Tarapacá": 2,
    "Antofagasta": 3,
    "Atacama": 4,
    "Coquimbo": 5,
    "Valparaíso": 6,
    "Región Metropolitana de Santiago": 7,
    "Región del Libertador Gral. Bernardo O’Higgins": 8,
    "Región del Maule": 9,
    "Región de Ñuble": 10,
    "Región del Biobío": 11,
    "Región de la Araucanía": 12,
    "Región de Los Ríos": 13,
    "Región de Los Lagos": 14,
    "Región Aisén del Gral. Carlos Ibáñez del Campo": 15,
    "Región de Magallanes y de la Antártica Chilena": 16,
}


# Leer archivo de origen
with open(archivo_origen, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

# El archivo de origen puede comenzar con una línea de comentario.
lineas = contenido.splitlines()

if lineas and lineas[0].strip().startswith("//"):
    lineas = lineas[1:]

contenido = "\n".join(lineas)

datos = json.loads(contenido)


# Crear fixture de Django
fixture = []

pk = 1

for region in datos["regiones"]:

    nombre_region = region["region"]

    if nombre_region not in region_ids:
        raise ValueError(
            f"No se encontró el ID para la región: {nombre_region}"
        )

    id_region = region_ids[nombre_region]

    for comuna in region["comunas"]:

        fixture.append({
            "model": "inmuebles.comuna",
            "pk": pk,
            "fields": {
                "nombre": comuna,
                "region": id_region
            }
        })

        pk += 1


# Guardar fixture
with open(archivo_destino, "w", encoding="utf-8") as archivo:
    json.dump(
        fixture,
        archivo,
        ensure_ascii=False,
        indent=4
    )


print(f"Fixture generado correctamente.")
print(f"Comunas generadas: {len(fixture)}")
print(f"Archivo: {archivo_destino}")