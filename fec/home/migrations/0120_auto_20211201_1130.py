# Generated by Django 3.1.13 on 2021-12-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0119_auto_20211013_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='category',
            field=models.CharField(choices=[('audit report', 'Audit report'), ('inspection or special review report', 'Inspection or special review report'), ('investigations', 'Investigations'), ('management challenges reports', 'Management challenges reports'), ('semiannual report', 'Semiannual report'), ('oig strategic plans', 'OIG strategic plans'), ('other oig reports and plans', 'Other OIG reports and plans'), ('work plan', 'Work plan'), ('agency financial report', 'Agency Financial Report'), ('congressional submission', 'Congressional submission'), ('performance and accountability report', 'Performance and accountability report'), ('strategic plan', 'Strategic plan'), ('summary of performance and financial information', 'Summary of performance and financial information'), ('annual report', 'Annual report'), ('summary report', 'Summary report'), ('privacy act notice', 'Privacy Act notice'), ('privacy policy', 'Privacy policy'), ('buy america report', 'Buy America report'), ('fair act', 'FAIR Act'), ('public procurement report', 'Public procurement report'), ('anniversary report', 'Anniversary report'), ('gift report', 'Gift report'), ('shutdown plan', 'Shutdown plan'), ('study', 'Study'), ('other reports and plans', 'Other reports and plans')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='category',
            field=models.CharField(blank=True, choices=[('audit report', 'Audit report'), ('inspection or special review report', 'Inspection or special review report'), ('investigations', 'Investigations'), ('management challenges reports', 'Management challenges reports'), ('semiannual report', 'Semiannual report'), ('oig strategic plans', 'OIG strategic plans'), ('other oig reports and plans', 'Other OIG reports and plans'), ('work plan', 'Work plan'), ('agency financial report', 'Agency Financial Report'), ('congressional submission', 'Congressional submission'), ('performance and accountability report', 'Performance and accountability report'), ('strategic plan', 'Strategic plan'), ('summary of performance and financial information', 'Summary of performance and financial information'), ('annual report', 'Annual report'), ('summary report', 'Summary report'), ('privacy act notice', 'Privacy Act notice'), ('privacy policy', 'Privacy policy'), ('buy america report', 'Buy America report'), ('fair act', 'FAIR Act'), ('public procurement report', 'Public procurement report'), ('anniversary report', 'Anniversary report'), ('gift report', 'Gift report'), ('shutdown plan', 'Shutdown plan'), ('study', 'Study'), ('other reports and plans', 'Other reports and plans')], help_text='If this is a report, add a category', max_length=255, null=True),
        ),
    ]
