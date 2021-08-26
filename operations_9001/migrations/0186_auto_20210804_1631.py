# Generated by Django 3.2.3 on 2021-08-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0185_auto_20210804_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_changeregister',
            name='raisedby_user_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='RaisedBy Sytem UserID.:'),
        ),
        migrations.AddField(
            model_name='mod9001_planning',
            name='proposedby_user_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ProposedBy Sytem UserID.:'),
        ),
        migrations.AddField(
            model_name='mod9001_qmsplanner',
            name='planner_user_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Planner Sytem UserID.:'),
        ),
        migrations.AddField(
            model_name='mod9001_trainingplanner',
            name='planner_user_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Planner Sytem UserID.:'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='BCL-M-04082021295', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='BCL-C-04082021237', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_changeregister',
            name='req_no',
            field=models.CharField(default='Comp-RFC-Q-04082021208', max_length=200, primary_key=True, serialize=False, verbose_name='Request No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_correctiveaction',
            name='car_no',
            field=models.CharField(default='Comp-CAR-Q-04082021265', max_length=200, primary_key=True, serialize=False, verbose_name='CAR No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='comp_no',
            field=models.CharField(default='Comp-COMP-Q-04082021175', max_length=200, primary_key=True, serialize=False, verbose_name='Complaint No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='satis_no',
            field=models.CharField(default='Comp-CS-Q-04082021199', max_length=200, primary_key=True, serialize=False, verbose_name='Satisfaction Survey No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='BCL-Q-04082021235', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-04082021108', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-04082021168', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='BCL-QP-04082021174', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-04082021153', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-04082021121', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]