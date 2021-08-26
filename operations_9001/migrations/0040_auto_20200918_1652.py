# Generated by Django 3.0.2 on 2020-09-18 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20200918_1652'),
        ('operations_9001', '0039_auto_20200918_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-18092020217', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-18092020229', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-18092020174', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-18092020278', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-18092020202', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-18092020237', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-18092020265', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noteffectreason', to='operations_9001.noteffective', verbose_name='If Not Effective, give reason:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='reasonother',
            field=models.TextField(blank=True, null=True, verbose_name='Other reasons:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='trainee',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='trainee', to='accounts.employees', verbose_name='Trainee:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-18092020127', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]
