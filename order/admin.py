from django.contrib import admin
from .models import Item, Order
# Register your models here.
admin.site.register(Order)
admin.site.register(Item)