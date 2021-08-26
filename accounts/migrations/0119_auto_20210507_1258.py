# Generated by Django 3.0.2 on 2021-05-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0118_auto_20210507_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA07052021759', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA946', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
