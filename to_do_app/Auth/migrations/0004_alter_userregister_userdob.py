# Generated by Django 3.2.6 on 2021-08-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_alter_userregister_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='userdob',
            field=models.DateField(default='2021-12-19'),
        ),
    ]
