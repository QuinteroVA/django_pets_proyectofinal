from django import forms


class ContactForm(forms.Form):
  name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
    attrs={'id':'name', 'class':'form-control p-4', 'placeholder':'Nombre', 'data-validation-required-message':"Ingrese su Nombre"}),
    min_length=3, max_length=100)
  email=forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
    attrs={'id':'email', 'class':'form-control p-4', 'placeholder':"Correo", 'data-validation-required-message':"Ingrese el correo"}))
  subject=forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
    attrs={'id':'subject', 'class':'form-control p-4', 'placeholder':"Asunto", 'data-validation-required-message':"Ingrese el asunto"}),
    min_length=3, max_length=100)  
  message=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
    attrs={'id':'message', 'class':'form-control p-4', 'rows':6, 'placeholder':"Mensaje", 'data-validation-required-message':"Escriba el mensaje"}),
    min_length=10, max_length=100)