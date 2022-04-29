from django.db import models

# Create your models here.
class Uom(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return  self.name

class Use(models.Model):
    name=models.CharField(max_length=255)

    
class DiseaseCategory(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Manufacturer(models.Model):
    name=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    area=models.CharField(max_length=255)
    street=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=255)
    manufacturer_fk=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    disease_category_fk=models.ForeignKey(DiseaseCategory,on_delete=models.CASCADE)
    description=models.TextField()
    price=models.FloatField()
    unit_size=models.PositiveIntegerField(default=10)
    uom_fk=models.ForeignKey(Uom,on_delete=models.CASCADE, blank=True, null=True)
    power=models.PositiveIntegerField(default=10)
    prescription_required=models.BooleanField(default=False)
    image_url = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class ProductUses(models.Model):
    product_fk=models.ForeignKey(Product,on_delete=models.CASCADE)
    uses_fk=models.ForeignKey(Use,on_delete=models.CASCADE)
