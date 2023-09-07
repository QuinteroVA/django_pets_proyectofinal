from django.contrib import admin
from .models import Service, Testimonial
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
admin.site.register(Service, ServiceAdmin)
    
class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Testimonial, TestimonialAdmin)