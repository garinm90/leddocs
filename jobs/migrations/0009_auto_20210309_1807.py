# Generated by Django 3.1.6 on 2021-03-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20210309_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='light',
            name='number_of_leds',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
