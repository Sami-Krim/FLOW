# Generated by Django 4.2.2 on 2023-07-11 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0014_alter_clients_sexeclient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='numRegistreCommerceClient',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='pieceIdentClient',
            field=models.PositiveBigIntegerField(choices=[(0, "Carte d'identité"), (1, 'Permis de conduire')]),
        ),
        migrations.AlterField(
            model_name='comptes',
            name='soldeCourant',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comptes',
            name='soldeHier',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mouvements',
            name='montantMouvement',
            field=models.PositiveBigIntegerField(),
        ),
    ]
