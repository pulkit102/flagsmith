# Generated by Django 2.2.16 on 2020-11-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0023_organisation_block_access_to_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='feature_analytics',
            field=models.BooleanField(default=False, help_text='Record feature analytics in InfluxDB'),
        ),
    ]