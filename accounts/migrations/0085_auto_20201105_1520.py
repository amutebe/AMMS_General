# Generated by Django 3.0.2 on 2020-11-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0084_auto_20201105_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA05112020725', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA224', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
