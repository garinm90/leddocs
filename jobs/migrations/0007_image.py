# Generated by Django 3.1.5 on 2021-01-11 19:36

from django.db import migrations, models
import django.db.models.deletion
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20210106_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=jobs.models.job_directory_path)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='jobs.job')),
            ],
        ),
    ]