# Generated by Django 3.2.6 on 2021-08-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0225_auto_20210828_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL28082021431', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL128', max_length=20, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
