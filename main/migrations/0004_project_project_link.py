# Generated by Django 3.0.4 on 2020-04-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200403_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
