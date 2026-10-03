import os
import django
import json

from django.contrib.auth.hashers import make_password

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arriendo.settings")
django.setup()


usuarios = [
    {
        "pk": 1001,
        "username": "gestor_demo",
        "first_name": "Gestor",
        "last_name": "Demo",
        "email": "gestor.demo@example.com",
    },
    {
        "pk": 1002,
        "username": "consulta_demo",
        "first_name": "Consulta",
        "last_name": "Demo",
        "email": "consulta.demo@example.com",
    },
    {
        "pk": 1003,
        "username": "usuario_demo",
        "first_name": "Usuario",
        "last_name": "Demo",
        "email": "usuario.demo@example.com",
    },
]


fixture = []

for usuario in usuarios:
    fixture.append({
        "model": "auth.user",
        "pk": usuario["pk"],
        "fields": {
            "password": make_password("Demo1234!"),
            "last_login": None,
            "is_superuser": False,
            "username": usuario["username"],
            "first_name": usuario["first_name"],
            "last_name": usuario["last_name"],
            "email": usuario["email"],
            "is_staff": False,
            "is_active": True,
            "date_joined": "2026-10-01T12:00:00Z",
            "groups": [],
            "user_permissions": []
        }
    })


with open(
    "usuarios.json",
    "w",
    encoding="utf-8"
) as archivo:
    json.dump(
        fixture,
        archivo,
        ensure_ascii=False,
        indent=4
    )


print("Fixture de usuarios generado correctamente.")
print(f"Usuarios generados: {len(fixture)}")
print("Archivo: usuarios.json")