# Generated by Django 4.2.2 on 2023-07-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0004_alter_comptes_soldecourant_alter_comptes_soldehier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='preClient',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
