# Generated by Django 3.1.6 on 2021-03-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20210309_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='number_of_leds',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lightcount',
            name='number_of_lights',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
