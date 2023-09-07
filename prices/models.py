from django.db import models

# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length=100)
    show_in_basic = models.BooleanField(default=False)
    show_in_standard = models.BooleanField(default=False)
    show_in_premium = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Plan"
        verbose_name_plural="Planes"
        ordering=["created"]
        
    def __str__(self):
        return self.title

class Price(models.Model):
    title=models.CharField(max_length=100, verbose_name="Título")
    price=models.CharField(max_length=100, verbose_name="Precio")
    image=models.ImageField(verbose_name="Imagen", upload_to="prices")
    services = models.ManyToManyField(Plan, verbose_name='Servicios')
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    
    class Meta:
        verbose_name="Precio"
        verbose_name_plural="Precios"
        ordering=["created"]
        
    def __str__(self):
        return self.title