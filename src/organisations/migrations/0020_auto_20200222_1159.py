# Generated by Django 2.2.10 on 2020-02-22 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0019_subscription_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='customer_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='OrganisationWebhook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.BooleanField(default=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webhooks', to='organisations.Organisation')),
            ],
        ),
    ]
