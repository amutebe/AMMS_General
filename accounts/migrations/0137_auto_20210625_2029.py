# Generated by Django 3.2.3 on 2021-06-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0136_auto_20210615_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA2506202171', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='carpriority',
            name='id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='ID:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA684', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]