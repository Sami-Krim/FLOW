# Generated by Django 4.2.2 on 2023-07-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0006_alter_clients_preclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateurs',
            name='username',
            field=models.CharField(default='efe', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
