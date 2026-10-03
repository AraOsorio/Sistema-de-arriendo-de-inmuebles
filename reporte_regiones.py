import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arriendo.settings")
django.setup()

from django.db import connection


sql = """
SELECT
    r.nombre AS region,
    i.nombre,
    i.descripcion
FROM inmuebles_inmueble i
INNER JOIN inmuebles_comuna c
    ON i.comuna_id = c.id
INNER JOIN inmuebles_region r
    ON c.region_id = r.id
ORDER BY r.id, i.nombre;
"""


with connection.cursor() as cursor:
    cursor.execute(sql)
    resultados = cursor.fetchall()


with open(
    "reporte_inmuebles_por_region.txt",
    "w",
    encoding="utf-8"
) as archivo:

    region_actual = None

    for region, nombre, descripcion in resultados:

        if region != region_actual:
            archivo.write("\n")
            archivo.write("=" * 60 + "\n")
            archivo.write(f"REGIÓN: {region}\n")
            archivo.write("=" * 60 + "\n")

            region_actual = region

        archivo.write(f"\nNombre: {nombre}\n")
        archivo.write(f"Descripción: {descripcion}\n")


print("Reporte generado correctamente.")
print(f"Inmuebles consultados: {len(resultados)}")
print("Archivo: reporte_inmuebles_por_region.txt")