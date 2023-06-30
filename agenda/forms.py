from django.forms import ModelForm, DateInput
from .models import Evento

class EventForm(ModelForm):
    class Meta:
        model = Evento
        fields = ('__all__')
        widgets = {
            'fecha' : DateInput(attrs={'type' : 'date'}),
        }