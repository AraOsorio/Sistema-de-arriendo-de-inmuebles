from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import PerfilUsuario, Inmueble


class RegistroForm(UserCreationForm):

    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu nombre"
        })
    )

    apellido = forms.CharField(
        label="Apellido",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu apellido"
        })
    )

    tipo_usuario = forms.ChoiceField(
        label="Tipo de usuario",
        choices=PerfilUsuario.TIPOS_USUARIO,
        widget=forms.Select(attrs={
            "class": "form-select"
        })
    )

    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu nombre de usuario"
        }),
        help_text="Máximo 150 caracteres."
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu contraseña"
        })
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Repite tu contraseña"
        })
    )

    class Meta:
        model = User
        fields = (
            "nombre",
            "apellido",
            "tipo_usuario",
            "username",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        usuario = super().save(commit=commit)

        if commit:
            PerfilUsuario.objects.create(
                usuario=usuario,
                nombre=self.cleaned_data["nombre"],
                apellido=self.cleaned_data["apellido"],
                tipo_usuario=self.cleaned_data["tipo_usuario"]
            )

        return usuario


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu nombre de usuario"
        })
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu contraseña"
        })
    )

class PerfilForm(forms.ModelForm):

    class Meta:
        model = PerfilUsuario
        fields = (
            "nombre",
            "apellido",
            "tipo_usuario",
        )

        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "apellido": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "tipo_usuario": forms.Select(attrs={
                "class": "form-select"
            }),
        }

class InmuebleForm(forms.ModelForm):

    class Meta:
        model = Inmueble

        fields = (
            "nombre",
            "descripcion",
            "m2_construidos",
            "m2_totales",
            "estacionamientos",
            "habitaciones",
            "banos",
            "direccion",
            "comuna",
            "tipo_inmueble",
            "precio_mensual",
        )

        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "descripcion": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),

            "m2_construidos": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),

            "m2_totales": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),

            "estacionamientos": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0"
            }),

            "habitaciones": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0"
            }),

            "banos": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0"
            }),

            "direccion": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "comuna": forms.Select(attrs={
                "class": "form-select"
            }),

            "tipo_inmueble": forms.Select(attrs={
                "class": "form-select"
            }),

            "precio_mensual": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),
        }