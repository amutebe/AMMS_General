# Generated by Django 3.0.2 on 2020-10-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_auto_20201002_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA02102020704', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA61', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]