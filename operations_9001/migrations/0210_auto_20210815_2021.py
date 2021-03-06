# Generated by Django 3.2.3 on 2021-08-15 17:21

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0209_auto_20210815_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='BCL-M-15082021244', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='BCL-C-15082021249', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_changeregister',
            name='req_no',
            field=models.CharField(default='Comp-RFC-Q-15082021228', max_length=200, primary_key=True, serialize=False, verbose_name='Request No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_correctiveaction',
            name='car_no',
            field=models.CharField(default='Comp-CAR-Q-15082021290', max_length=200, primary_key=True, serialize=False, verbose_name='CAR No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='comp_no',
            field=models.CharField(default='Comp-COMP-Q-15082021202', max_length=200, primary_key=True, serialize=False, verbose_name='Complaint No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/', validators=[accounts.utils.validate_file_size], verbose_name='Upload Support Document:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='satis_no',
            field=models.CharField(default='Comp-CS-Q-15082021184', max_length=200, primary_key=True, serialize=False, verbose_name='Satisfaction Survey No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='BCL-Q-15082021225', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_incidentregisterstaff',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/', validators=[accounts.utils.validate_file_size], verbose_name='Upload Support Document:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-15082021214', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-15082021196', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='BCL-QP-15082021161', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-15082021127', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-15082021217', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]
