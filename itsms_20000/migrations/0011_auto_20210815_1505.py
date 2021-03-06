# Generated by Django 3.2.3 on 2021-08-15 12:05

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsms_20000', '0010_alter_mod20000_service_planning_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod20000_service_planning',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/', validators=[accounts.utils.validate_file_size], verbose_name='Upload Support Document:'),
        ),
        migrations.AlterField(
            model_name='mod20000_service_planning',
            name='verification_failed',
            field=models.TextField(blank=True, null=True, verbose_name='Reason for rejecting:'),
        ),
    ]
