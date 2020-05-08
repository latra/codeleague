# Generated by Django 3.0.4 on 2020-05-08 21:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('data_start_inscription', models.DateField(default=datetime.datetime.now)),
                ('hour_start_inscription', models.TimeField()),
                ('data_finish_inscription', models.DateField(default=datetime.datetime.now)),
                ('hour_finish_inscription', models.TimeField()),
                ('data_start_competition', models.DateField(default=datetime.datetime.now)),
                ('hour_start_competition', models.TimeField()),
                ('data_finish_competition', models.DateField(default=datetime.datetime.now)),
                ('hour_finish_competition', models.TimeField()),
                ('categories', models.ManyToManyField(blank=True, to='league.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file_bucket', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('githuburl', models.URLField(blank=True)),
                ('submit_date', models.DateField(auto_now=True)),
                ('team_id', models.IntegerField(null=True)),
                ('files', models.ManyToManyField(blank=True, to='league.Files')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('competition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.Competition')),
                ('members', models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL)),
                ('ranking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.Ranking')),
                ('submition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='league.Submit')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='files',
            field=models.ManyToManyField(blank=True, to='league.Files'),
        ),
        migrations.AddField(
            model_name='competition',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
