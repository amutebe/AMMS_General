# Generated by Django 3.2.3 on 2021-08-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsms_20000', '0006_auto_20210810_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod20000_service_planning',
            name='record_group',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Data Group'),
        ),
        migrations.AddField(
            model_name='mod20000_service_request',
            name='record_group',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Data Group'),
        ),
    ]
