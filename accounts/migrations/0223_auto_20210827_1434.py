# Generated by Django 3.2.6 on 2021-08-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0222_auto_20210821_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL27082021736', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL419', max_length=20, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
