from django.contrib import admin
from .models import Aluno
# Configurações de visualização
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'idade') # campos que aparecem na listagem
    ordering = ('ano', 'nome') # criterio de ordenacao
    search_fields =('nome', 'ano') # cria caixa de pesquisa para campos indicados
    # Registo dos modelos
admin.site.register(Aluno, AlunoAdmin)
