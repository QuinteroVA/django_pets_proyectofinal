from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm
# Create your views here.   
def contact(request):
    contactForm=ContactForm()
    if request.method=="POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            subject=request.POST.get('subject','')
            message=request.POST.get('message','')
            email=EmailMessage(
                "PetLover: Nuevo mensaje",
                "De {} <{}>\n\nAsunto: {}\n\nMensaje:\n\n{}".format(name,email,subject,message),
                "correo@inbox.mailtrap.io",
                ["aquintero@itsqmet.edu.ec"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
    return render(request,"contact/contact.html", {'contactForm':contactForm})