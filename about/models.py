from django.db import models
from social.models import Social

# Create your models here.
class About(models.Model):
    name=models.CharField(max_length=50, verbose_name="Nombre")
    profession=models.CharField(max_length=50,verbose_name="Cargo")
    socialnet = models.ManyToManyField(Social, verbose_name='Redes')
    image=models.ImageField(verbose_name="Imagen")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Miembro"
        verbose_name_plural="Miembros"
        ordering=["created"]

    def __str__(self):
        return self.name