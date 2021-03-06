# Generated by Django 3.2.3 on 2021-08-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0184_auto_20210803_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL04082021192', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL802', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
