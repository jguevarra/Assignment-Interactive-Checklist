# Generated by Django 2.1.1 on 2018-11-03 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0013_auto_20181101_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_test', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_assignment_calendar.Events')),
            ],
        ),
    ]
