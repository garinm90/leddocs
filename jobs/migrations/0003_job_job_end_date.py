# Generated by Django 3.1.4 on 2021-01-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210104_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
