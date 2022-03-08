from django.db import models
from django.contrib.auth.models import User

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

