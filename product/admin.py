from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Uom)
admin.site.register(Use)
admin.site.register(DiseaseCategory)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(ProductUses)