# Generated by Django 2.2.10 on 2021-07-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0011_auto_20210727_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
