# Generated by Django 4.2.7 on 2023-12-03 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tiendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('provincia', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('pre_venta', models.CharField(blank=True, max_length=50, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=50, null=True)),
                ('tienda_relacionada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionTienda.tiendas')),
            ],
        ),
    ]
