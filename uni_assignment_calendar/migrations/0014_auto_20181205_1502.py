# Generated by Django 2.1.1 on 2018-12-05 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0013_auto_20181205_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='checked_users',
        ),
        migrations.RemoveField(
            model_name='events',
            name='course',
        ),
        migrations.RemoveField(
            model_name='events',
            name='description',
        ),
        migrations.RemoveField(
            model_name='events',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='events',
            name='due_time',
        ),
        migrations.RemoveField(
            model_name='events',
            name='events_name',
        ),
        migrations.RemoveField(
            model_name='events',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='events',
            name='users',
        ),
    ]
