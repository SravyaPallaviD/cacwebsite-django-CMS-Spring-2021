# Generated by Django 3.1.7 on 2021-04-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20210413_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='darknesstolight',
            name='description',
            field=models.TextField(default='blank'),
        ),
        migrations.AddField(
            model_name='darknesstolight',
            name='title',
            field=models.CharField(default='blank', max_length=120),
        ),
    ]
