# Generated by Django 3.0.7 on 2021-12-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0009_auto_20211208_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='sector_actividad',
            field=models.CharField(choices=[('', '----------'), ('CE', 'Carnes y embutidos'), ('FV', 'Frutas y verduras'), ('PC', 'Pescados y conservas'), ('OA', 'Otros porudctos de alimentacion'), ('BA', 'Bebidas y alcoholes'), ('CP', 'Calzado y piel'), ('T', 'Textiles'), ('C', 'Corcho'), ('CM', 'Construcción y mobiliario'), ('SI', 'Suministros industriales'), ('PQ', 'Productos químicos y básicos'), ('SC', 'Servicios de consultoría'), ('SM', 'Servicios de montaje/mantenimiento/técnico'), ('SGR', 'Servicios de gestión de residuos'), ('SIE', 'Servicios de ingeniería/energía/renovables y economía circular'), ('TIC', 'Servicios TIC'), ('OTHER', 'Otros')], max_length=100),
        ),
    ]
