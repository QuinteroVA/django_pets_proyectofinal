from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    icon_class = models.CharField(max_length=50, verbose_name="Icono",null=True)
    title=models.CharField(max_length=100, verbose_name="Título")
    content=RichTextField(verbose_name="Contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"
        ordering=["created"]

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre")
    profession=models.CharField(max_length=100, verbose_name="Profesión")
    content=RichTextField(verbose_name="Testimonio")
    image=models.ImageField(verbose_name="imagen", upload_to='services')
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"
        ordering=["created"]

    def __str__(self):
        return self.name