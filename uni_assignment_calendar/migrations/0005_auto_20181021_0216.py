# Generated by Django 2.1.1 on 2018-10-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0004_event_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.TextField(blank=True, help_text='Event name', null=True, verbose_name='Event Name'),
        ),
    ]