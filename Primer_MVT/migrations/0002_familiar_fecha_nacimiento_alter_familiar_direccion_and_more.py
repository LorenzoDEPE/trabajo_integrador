# Generated by Django 4.1.2 on 2022-10-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Primer_MVT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='direccion',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
    ]
