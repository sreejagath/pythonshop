from django.contrib import admin
from .models import Product,offers
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')
class OfferAdmin(admin.ModelAdmin):
    list_display=('code','description','discount')
admin.site.register(Product,ProductAdmin)
admin.site.register(offers,OfferAdmin)