# Generated by Django 2.2.10 on 2021-07-29 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0014_auto_20210728_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateField(default=datetime.date(2021, 7, 30)),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=255),
        ),
    ]
