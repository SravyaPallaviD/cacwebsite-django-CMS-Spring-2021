# Generated by Django 3.1.7 on 2021-03-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20210329_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='videos', verbose_name='')),
            ],
        ),
    ]