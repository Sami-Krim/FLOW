# Generated by Django 4.2.2 on 2023-07-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0013_rename_datedernoperutil_utilisateurs_derniereoperutil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='sexeClient',
            field=models.IntegerField(choices=[(0, 'Homme'), (1, 'Femme')]),
        ),
    ]
