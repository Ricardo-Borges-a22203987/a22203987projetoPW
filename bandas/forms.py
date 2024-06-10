from django import forms
from .models import Banda,Album,Musica

class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda
    fields = '__all__'
    help_texts = {
            'nome': 'Insira o nome completo da banda.',
            'genero': 'Selecione o gênero musical principal da banda.',
            'foto_banda': 'Insira uma foto da banda.',
        }

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome da Banda',
      })
    }


class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

    labels = {
      'titulo': 'Título',
      'ano_lancamento': 'Ano de Publicação',
    }



class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica
    fields = '__all__'

    labels = {
      'titulo': 'Título',
    }

