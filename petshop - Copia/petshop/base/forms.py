from django import forms

class contatoform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

class reservaform(forms.Form):
    nome_do_pet = forms.CharField()
    telefone = forms.CharField()
    dia_da_reserva = forms.CharField()
    observação = forms.CharField(widget=forms.Textarea)