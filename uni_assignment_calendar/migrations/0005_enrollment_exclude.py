# Generated by Django 2.1.1 on 2018-12-03 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0004_auto_20181202_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='exclude',
            field=models.IntegerField(default=-1, max_length=10),
        ),
    ]