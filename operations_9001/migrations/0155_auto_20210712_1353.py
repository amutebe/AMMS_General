# Generated by Django 3.2.3 on 2021-07-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0154_auto_20210709_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='BCL-M-12072021277', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='BCL-C-12072021224', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_changeregister',
            name='req_no',
            field=models.CharField(default='Comp-RFC-Q-12072021186', max_length=200, primary_key=True, serialize=False, verbose_name='Request No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_correctiveaction',
            name='car_no',
            field=models.CharField(default='Comp-CAR-Q-12072021253', max_length=200, primary_key=True, serialize=False, verbose_name='CAR No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='comp_no',
            field=models.CharField(default='Comp-COMP-Q-12072021134', max_length=200, primary_key=True, serialize=False, verbose_name='Complaint No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='satis_no',
            field=models.CharField(default='Comp-CS-Q-12072021198', max_length=200, primary_key=True, serialize=False, verbose_name='Satisfaction Survey No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='BCL-Q-12072021132', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-12072021256', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-12072021219', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='BCL-QP-12072021106', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-12072021291', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-12072021277', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]