# Generated by Django 3.0.2 on 2020-10-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_auto_20201014_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA14102020433', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA225', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
