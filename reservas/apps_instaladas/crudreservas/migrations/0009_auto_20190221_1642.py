# Generated by Django 2.1.5 on 2019-02-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudreservas', '0008_auto_20190221_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default='Masculino', max_length=12),
        ),
    ]
