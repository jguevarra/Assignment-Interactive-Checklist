# Generated by Django 2.1.1 on 2018-12-04 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0006_auto_20181204_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blacklist',
            old_name='blacklist',
            new_name='block',
        ),
    ]
