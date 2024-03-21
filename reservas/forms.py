# reservas/forms.py
from django import forms
from .models import Reserva, Habitacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacion', 'fecha_inicio', 'fecha_fin']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['habitacion'].queryset = Habitacion.objects.filter(disponible=True)
        if user:
            self.fields['usuario'].queryset = User.objects.filter(pk=user.pk)  # Filtrar opciones basadas en el usuario actual
        
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')