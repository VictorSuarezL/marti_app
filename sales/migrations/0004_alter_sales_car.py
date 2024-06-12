# Generated by Django 5.0.6 on 2024-06-11 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_car_f_compra_alter_car_f_matriculacion_and_more'),
        ('sales', '0003_alter_sales_doble_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.car'),
        ),
    ]
