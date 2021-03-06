# Generated by Django 3.0.4 on 2020-05-10 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_auto_20200509_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='finalized',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='submition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='league.Submit'),
        ),
    ]
