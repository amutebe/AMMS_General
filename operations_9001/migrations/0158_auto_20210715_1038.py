# Generated by Django 3.2.3 on 2021-07-15 07:38

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0157_auto_20210713_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mod9001_customersatisfaction',
            name='customerservice',
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='BCL-M-15072021128', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='BCL-C-15072021244', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_changeregister',
            name='req_no',
            field=models.CharField(default='Comp-RFC-Q-15072021109', max_length=200, primary_key=True, serialize=False, verbose_name='Request No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_correctiveaction',
            name='car_no',
            field=models.CharField(default='Comp-CAR-Q-15072021229', max_length=200, primary_key=True, serialize=False, verbose_name='CAR No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='comp_no',
            field=models.CharField(default='Comp-COMP-Q-15072021154', max_length=200, primary_key=True, serialize=False, verbose_name='Complaint No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='communication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comm', to='operations_9001.providerparameters', verbose_name='4. Response to support:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='compliant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handlin', to='operations_9001.providerparameters', verbose_name='5. Service Reporting:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivtime', to='operations_9001.providerparameters', verbose_name='3. Complaint Handling/ Resolution:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='improvplan',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Time Management'), ('2', 'Knowledge of the products'), ('3', 'Complaint Handling/ Resolution'), ('4', 'Response to support'), ('5', 'Service Reporting'), ('6', 'Professionalism'), ('7', 'Overall quality of our products/ services'), ('8', 'Other')], max_length=15, null=True, verbose_name='Improvement Plan'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='infosecurity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='securit', to='operations_9001.providerparameters', verbose_name='7. Overall quality of our products/ services:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='quality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serv', to='operations_9001.providerparameters', verbose_name='6. Professionalism:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='rank',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Final Rating:(Scores 1 to 7 are required)'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='resolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resotime', to='operations_9001.providerparameters', verbose_name='2. Knowledge of the products:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='responsetime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resptime', to='operations_9001.providerparameters', verbose_name='1. Time Management:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='satis_no',
            field=models.CharField(default='Comp-CS-Q-15072021238', max_length=200, primary_key=True, serialize=False, verbose_name='Satisfaction Survey No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='BCL-Q-15072021120', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-15072021262', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-15072021107', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='BCL-QP-15072021209', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-15072021160', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-15072021257', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]
