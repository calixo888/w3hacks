# Generated by Django 3.0.4 on 2020-04-19 00:48

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20200418_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixTheCodeExercise',
            fields=[
                ('id', models.CharField(default=main.models.generate_id, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('prerequisites', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None)),
                ('repl_link', models.CharField(max_length=100)),
                ('difficulty_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.DifficultyLevel')),
                ('resources', models.ManyToManyField(blank=True, to='main.ResourceLink')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedFixTheCodeExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repl_link', models.CharField(max_length=100)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('fix_the_code_exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.FixTheCodeExercise')),
            ],
        ),
    ]
