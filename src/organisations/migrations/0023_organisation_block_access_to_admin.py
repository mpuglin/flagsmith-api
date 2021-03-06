# Generated by Django 2.2.14 on 2020-10-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0022_organisation_persist_trait_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='block_access_to_admin',
            field=models.BooleanField(default=False, help_text='Enable this to block all the access to admin interface for the organisation'),
        ),
    ]
