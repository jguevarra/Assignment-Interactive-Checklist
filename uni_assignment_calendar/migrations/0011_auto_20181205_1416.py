# Generated by Django 2.1.1 on 2018-12-05 19:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0010_auto_20181205_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='checked_users',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=list, size=None),
        ),
        migrations.AddField(
            model_name='events',
            name='users',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=list, size=None),
        ),
    ]
