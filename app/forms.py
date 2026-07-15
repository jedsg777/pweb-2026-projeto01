from django import forms

class PersonagemForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome do Ator")
    personagem = forms.CharField(max_length=100, label="Personagem na Série")
    idade = forms.IntegerField(label="Idade")
    posicao = forms.CharField(max_length=100, label="Posição/Papel")
    local_nascimento = forms.CharField(max_length=100, label="Local de Nascimento")
    
class PersonagemForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome do Ator")
    personagem = forms.CharField(max_length=100, label="Personagem na Série")
    idade = forms.IntegerField(label="Idade")
    posicao = forms.CharField(max_length=100, label="Posição/Papel")
    local_nascimento = forms.CharField(max_length=100, label="Local de Nascimento")
    
    # Campo para upload real de arquivo de imagem
    foto = forms.FileField(label="Foto do Personagem", required=True)
    