# Generated by Django 2.2.10 on 2020-11-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0007_auto_20201118_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
