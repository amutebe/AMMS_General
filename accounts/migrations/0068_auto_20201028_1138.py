# Generated by Django 3.0.2 on 2020-10-28 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0067_auto_20201016_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA28102020761', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA495', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
