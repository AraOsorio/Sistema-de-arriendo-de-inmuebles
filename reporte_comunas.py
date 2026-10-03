import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arriendo.settings")
django.setup()

from django.db import connection


sql = """
SELECT
    c.nombre AS comuna,
    i.nombre,
    i.descripcion
FROM inmuebles_inmueble i
INNER JOIN inmuebles_comuna c
    ON i.comuna_id = c.id
ORDER BY c.nombre, i.nombre;
"""


with connection.cursor() as cursor:
    cursor.execute(sql)
    resultados = cursor.fetchall()


with open("reporte_inmuebles_por_comuna.txt", "w", encoding="utf-8") as archivo:

    comuna_actual = None

    for comuna, nombre, descripcion in resultados:

        if comuna != comuna_actual:
            archivo.write("\n")
            archivo.write("=" * 60 + "\n")
            archivo.write(f"COMUNA: {comuna}\n")
            archivo.write("=" * 60 + "\n")

            comuna_actual = comuna

        archivo.write(f"\nNombre: {nombre}\n")
        archivo.write(f"Descripción: {descripcion}\n")


print("Reporte generado correctamente.")
print(f"Inmuebles consultados: {len(resultados)}")
print("Archivo: reporte_inmuebles_por_comuna.txt")