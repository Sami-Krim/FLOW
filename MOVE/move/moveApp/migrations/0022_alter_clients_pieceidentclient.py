# Generated by Django 4.2.2 on 2023-07-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0021_alter_clients_nbrmodifinfoclient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='pieceIdentClient',
            field=models.IntegerField(choices=[(0, "Carte d'identité"), (1, 'Permis de conduire')]),
        ),
    ]
