from .models import * 
from django import forms

class PersonagemForm(forms.ModelForm):  
    class Meta:
        model = PersonagemHarryPotter
        fields = '__all__'

    def __init__(self, *args, **Rwargs):
        super(PersonagemForm, self).__init__(*args, **Rwargs)

        if self.instance and self.instance.pk:
            self.fields['cpf'].disabled = True