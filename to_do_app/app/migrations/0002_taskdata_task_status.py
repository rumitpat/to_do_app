# Generated by Django 3.2.6 on 2021-08-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskdata',
            name='task_status',
            field=models.CharField(default=False, max_length=200),
        ),
    ]