# Generated by Django 2.1.1 on 2018-11-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0012_auto_20181029_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
