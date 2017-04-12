from django.contrib import admin

# Register your models here.
from .models import Product, Unity, PredefinedProduct

admin.site.register(Product)
admin.site.register(PredefinedProduct)
admin.site.register(Unity)