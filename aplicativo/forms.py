from .models import * 
from django import forms

class PersonagemForm(forms.ModelForm):  
    class Meta:
        model = PersonagemHarryPotter
        fields = '__all__'