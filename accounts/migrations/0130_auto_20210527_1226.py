# Generated by Django 3.2.3 on 2021-05-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0129_auto_20210526_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA27052021465', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA938', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
