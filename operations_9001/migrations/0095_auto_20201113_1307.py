# Generated by Django 3.0.2 on 2020-11-13 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0094_auto_20201113_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mod9001_customersatisfaction',
            name='year',
        ),
        migrations.AddField(
            model_name='mod9001_customersatisfaction',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='End Date:'),
        ),
        migrations.AddField(
            model_name='mod9001_customersatisfaction',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date:'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-13112020104', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-13112020203', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_changeregister',
            name='req_no',
            field=models.CharField(default='Comp-RFC-Q-13112020177', max_length=200, primary_key=True, serialize=False, verbose_name='Request No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_correctiveaction',
            name='car_no',
            field=models.CharField(default='Comp-CAR-Q-13112020278', max_length=200, primary_key=True, serialize=False, verbose_name='CAR No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='operations_9001.classification', verbose_name='Complaint Classification:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='comp_no',
            field=models.CharField(default='Comp-COMP-Q-13112020104', max_length=200, primary_key=True, serialize=False, verbose_name='Complaint No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='complaint',
            field=models.TextField(blank=True, null=True, verbose_name='Complainant:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='due',
            field=models.DateTimeField(null=True, verbose_name='When:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='due',
            field=models.DateTimeField(null=True, verbose_name='When:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='satis_no',
            field=models.CharField(default='Comp-CS-Q-13112020208', max_length=200, primary_key=True, serialize=False, verbose_name='Satisfaction Survey No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-13112020112', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-13112020208', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-13112020109', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-13112020120', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-13112020115', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-13112020106', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]