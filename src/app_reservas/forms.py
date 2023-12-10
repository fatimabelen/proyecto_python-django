from django import forms
from .models import ReservaServicio

class ReservaServicioForm(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = ['fecha_reservada', 'cliente', 'servicio', 'empleado', 'responsable']

    def __init__(self, *args, **kwargs):
        super(ReservaServicioForm, self).__init__(*args, **kwargs)
        
        # Filtra clientes, servicios, empleados y coordinadores activos
        self.fields['cliente'].queryset = self.fields['cliente'].queryset.filter(activo=True)
        self.fields['servicio'].queryset = self.fields['servicio'].queryset.filter(activo=True)
        self.fields['empleado'].queryset = self.fields['empleado'].queryset.filter(activo=True)
        self.fields['responsable'].queryset = self.fields['responsable'].queryset.filter(activo=True)
