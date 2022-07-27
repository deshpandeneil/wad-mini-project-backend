from product.models import DiseaseCategory, Manufacturer, Product
import csv

def run():
    with open('data\WADMedicineData.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Manufacturer.objects.all().delete()
        Product.objects.all().delete()

        for row in reader:
            print(row)

            manufactuer, _ = Manufacturer.objects.get_or_create(name=row[2])

            disease,_= DiseaseCategory.objects.get_or_create(name="Allergy")
            product = Product(name=row[0],
                        price=row[1],
                        description=row[3],
                        manufacturer_fk=manufactuer,
                        disease_category_fk=disease,
                        image_url=row[4])
            product.save()
