# Generated by Django 3.1.4 on 2021-01-04 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_end_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='number_of_lights',
        ),
    ]
