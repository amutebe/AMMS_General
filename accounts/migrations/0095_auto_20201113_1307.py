# Generated by Django 3.0.2 on 2020-11-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0094_auto_20201113_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA13112020116', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA398', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
