# Generated by Django 2.1.5 on 2019-02-21 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudreservas', '0006_auto_20190221_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudreservas.UsuarioRol'),
        ),
    ]