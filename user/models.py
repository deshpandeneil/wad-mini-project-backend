from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    state=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    area=models.CharField(max_length=255)
    street=models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
