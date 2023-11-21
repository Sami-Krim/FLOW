# Generated by Django 4.2.2 on 2023-07-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0015_alter_clients_numregistrecommerceclient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='activiteClient',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='adresse2Client',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='clients',
            name='clientPresume',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='gerantClient',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='lieuNaissanceClient',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='mereClient',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='numRegistreCommerceClient',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='pereClient',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='preClient',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='professionClient',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='sexeClient',
            field=models.IntegerField(blank=True, choices=[(0, 'Homme'), (1, 'Femme')], null=True),
        ),
    ]
