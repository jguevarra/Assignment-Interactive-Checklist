# Generated by Django 2.1.1 on 2018-10-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_assignment_calendar', '0011_auto_20181028_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField()),
                ('class_abbrev', models.CharField(max_length=4)),
                ('class_num', models.IntegerField()),
                ('cladd_name', models.TextField(max_length=30)),
                ('instructor', models.TextField(max_length=30)),
            ],
        ),
    ]
