from django import forms
from .models import Habitacion, Cliente, Reserva

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['tipo', 'precio_por_noche', 'disponible']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono']


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacion', 'cliente', 'fecha_entrada', 'fecha_salida', 'numero_huespedes']