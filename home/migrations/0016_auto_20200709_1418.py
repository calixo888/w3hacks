# Generated by Django 3.0.7 on 2020-07-09 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200709_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 14, 18, 18, 483729)),
        ),
    ]
