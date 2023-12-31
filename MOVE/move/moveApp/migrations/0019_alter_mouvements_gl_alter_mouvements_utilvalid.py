# Generated by Django 4.2.2 on 2023-07-12 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moveApp', '0018_alter_comptes_datederniereoperation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouvements',
            name='GL',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='moveApp.grandlivres'),
        ),
        migrations.AlterField(
            model_name='mouvements',
            name='utilValid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mouvements_valid', to=settings.AUTH_USER_MODEL),
        ),
    ]
