from .views import *
from django.urls import path

urlpatterns = [
    path('lista/', view=lista_personagens, name='lista_personagens'),
    path('criar/', view=criar_bruxo, name='criar_bruxo'),
    path('atualizar/<int:pk>', view=atualizar_bruxo, name='atualizar_bruxo'),

]