# Generated by Django 2.2.10 on 2020-11-17 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20201117_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 18, 20, 55, 0, 33736)),
        ),
    ]
