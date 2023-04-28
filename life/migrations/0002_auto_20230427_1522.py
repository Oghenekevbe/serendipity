# Generated by Django 3.2.16 on 2023-04-27 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
