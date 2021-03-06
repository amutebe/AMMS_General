# Generated by Django 3.2.3 on 2021-08-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0195_auto_20210812_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_issues',
            name='analyst_user_title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Title:'),
        ),
        migrations.AddField(
            model_name='mod9001_regulatoryreq',
            name='analyst_user_title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Title:'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='BCL-IP-Q-12082021533', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='BCL-IP-Q-12082021863', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='BCL-CT-Q-12082021178', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='BCL-IP-LRO-Q-12082021340', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='BCL-RA-12082021932', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(default='BCL-IP-Q-12082021670', max_length=200, primary_key=True, serialize=False, verbose_name='ID.:'),
        ),
    ]
