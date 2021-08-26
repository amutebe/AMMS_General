# Generated by Django 3.2.3 on 2021-07-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0167_auto_20210718_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL18072021827', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL403', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]