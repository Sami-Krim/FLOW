# Generated by Django 4.2.2 on 2023-07-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0023_alter_clients_situationfamiliale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grandlivres',
            name='libelleGL',
            field=models.CharField(max_length=200),
        ),
    ]
