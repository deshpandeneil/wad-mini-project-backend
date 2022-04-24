from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('name','manufacturer_fk','disease_category_fk','price')