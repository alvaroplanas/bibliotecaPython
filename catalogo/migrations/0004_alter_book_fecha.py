# Generated by Django 3.2.8 on 2021-11-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20211102_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='fecha',
            field=models.DateField(auto_now=True, help_text='Fecha de publicacion', null=True),
        ),
    ]
