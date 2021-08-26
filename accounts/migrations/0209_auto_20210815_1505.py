# Generated by Django 3.2.3 on 2021-08-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0208_auto_20210814_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL15082021653', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL241', max_length=20, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
