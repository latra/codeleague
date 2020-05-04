# Generated by Django 3.0.4 on 2020-05-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_delete_leagueuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='categories',
            field=models.ManyToManyField(blank=True, to='league.Category'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='data_start_inscription',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]