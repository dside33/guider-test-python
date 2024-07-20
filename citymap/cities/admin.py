from django.contrib import admin
from .models import City, Street, Shop

class StreetInline(admin.TabularInline): 
    model = Street
    extra = 0  

class CityAdmin(admin.ModelAdmin):
    inlines = [StreetInline]

admin.site.register(City, CityAdmin)
admin.site.register(Street) 
admin.site.register(Shop)
