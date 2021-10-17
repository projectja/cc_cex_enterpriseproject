# Generated by Django 3.0.7 on 2021-10-14 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('partidas', models.CharField(max_length=100)),
                ('poblacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Poblacion')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Sector')),
            ],
        ),
    ]
