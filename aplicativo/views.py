from django.shortcuts import render, redirect  
from .models import PersonagemHarryPotter
from .forms import PersonagemForm  

def lista_personagens(request):
    personagens = PersonagemHarryPotter.objects.all()
    return render(request, 'listagem.html', {'personagens': personagens})

def criar_bruxo(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('lista_personagens') 
    else:
        form = PersonagemForm()
    return render(request, 'formulario.html', {'formulario': form})

def atualizar_bruxo(request, pk):
    bruxo = get_object_or_404(PersonagemHarryPotter, pk=pk)
    if request.method == 'POST':
        form = PersonagemForm(request.POST, instance=bruxo) 
        if form.is_valid():
            form.save()
            return redirect('lista_personagens')  
    else:
        form = PersonagemForm(instance=bruxo)  
    print(form)
    return render(request, 'formulario.html', {'formulario': form})