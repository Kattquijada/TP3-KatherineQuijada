# Generated by Django 5.1.4 on 2024-12-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_remove_deuda_fuente_deuda_entidad_alter_deuda_deudas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deuda',
            name='entidad',
            field=models.CharField(choices=[('Itau', 'Itau'), ('Scotiabank', 'Scotiabank'), ('Familia', 'Familia')], max_length=20),
        ),
        migrations.AlterField(
            model_name='egresos',
            name='fuente',
            field=models.CharField(choices=[('Cuenta Corriente', 'Cuenta Corriente'), ('Efectivo', 'Efectivo')], max_length=20),
        ),
    ]