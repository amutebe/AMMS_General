# Generated by Django 3.2.6 on 2021-08-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0223_auto_20210827_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL280820212', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL295', max_length=20, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
