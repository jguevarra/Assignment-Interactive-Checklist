# Generated by Django 2.1.1 on 2018-11-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0002_events_due_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
