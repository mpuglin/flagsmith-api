# Generated by Django 2.2.12 on 2020-06-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0012_auto_20200504_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltrait',
            name='float_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trait',
            name='float_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicaltrait',
            name='value_type',
            field=models.CharField(blank=True, choices=[('int', 'Integer'), ('unicode', 'String'), ('bool', 'Boolean'), ('float', 'Float')], default='unicode', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='trait',
            name='value_type',
            field=models.CharField(blank=True, choices=[('int', 'Integer'), ('unicode', 'String'), ('bool', 'Boolean'), ('float', 'Float')], default='unicode', max_length=10, null=True),
        ),
    ]
