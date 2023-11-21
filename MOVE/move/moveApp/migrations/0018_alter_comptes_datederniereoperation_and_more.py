# Generated by Django 4.2.2 on 2023-07-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0017_alter_clients_adresse2client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comptes',
            name='dateDerniereOperation',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comptes',
            name='dateFermetureCompte',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comptes',
            name='dateMiseEnOpposition',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comptes',
            name='soldeHier',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]