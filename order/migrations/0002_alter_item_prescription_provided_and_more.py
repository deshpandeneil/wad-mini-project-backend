# Generated by Django 4.0.3 on 2022-04-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='prescription_provided',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
