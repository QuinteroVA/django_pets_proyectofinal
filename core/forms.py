from django import forms

class BookingForm(forms.Form):
  name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
    attrs={'id':'name', 'class':'custom-select border-0 px-4', 'placeholder':'Nombre', 'data-validation-required-message':"Ingrese su Nombre"}),
    min_length=3, max_length=100)
  email=forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
    attrs={'id':'email', 'class':'custom-select border-0 px-44', 'placeholder':"Correo", 'data-validation-required-message':"Ingrese el correo"})) 
  date=forms.DateField(label="Fecha", widget=forms.TextInput(
    attrs={'id':'date', 'class':'custom-select border-0 px-4 datetimepicker-input', 'data-target':'#date', 'data-toggle':'datetimepicker', 'placeholder':"Fecha de Reservación", 'data-validation-required-message':"Ingrese la fecha"}))  
  hour=forms.TimeField(label="Hora", widget=forms.TextInput(
    attrs={'id':'time', 'class':'custom-select border-0 px-4datetimepicker-input', 'data-target':'#time', 'data-toggle':'datetimepicker', 'placeholder':"Hora de Reservación", 'data-validation-required-message':"Escriba la hora"}))
  bservice=forms.ChoiceField(label="Servicios", required=True, choices=[
      ("Alojamiento", "Alojamiento"),("Alimentación", "Alimentación"),("Aseo", "Aseo"),("Entretenimiento", "Entretenimiento"),("Ejercicios", "Ejercicios"),("Tratamientos", "Tratamientos")
    ],widget=forms.Select(attrs={'class': 'custom-select border-0 px-4'}),
  )