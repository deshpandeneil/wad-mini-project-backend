from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Order(models.Model):
    user_fk=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.FloatField()
    total_quantity=models.PositiveIntegerField()
    eta=models.DateField()
    
class Item(models.Model):
    product_fk=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_fk=models.ForeignKey(Order,on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.PositiveIntegerField()
    prescription_provided=models.BooleanField()


