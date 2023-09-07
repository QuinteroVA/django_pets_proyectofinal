from django.contrib import admin
from .models import Price, Plan
# Register your models here.

class PriceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
admin.site.register(Price, PriceAdmin)

class PlanAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
admin.site.register(Plan, PlanAdmin)