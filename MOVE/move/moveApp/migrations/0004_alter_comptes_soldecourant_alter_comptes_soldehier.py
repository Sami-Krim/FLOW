# Generated by Django 4.2.2 on 2023-07-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0003_alter_clients_nbrmodifinfoclient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comptes',
            name='soldeCourant',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comptes',
            name='soldeHier',
            field=models.PositiveIntegerField(null=True),
        ),
    ]