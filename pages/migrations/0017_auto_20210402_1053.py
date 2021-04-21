# Generated by Django 3.1.7 on 2021-04-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_mediainformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='CannonService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(default='default.jpg', upload_to='pics')),
            ],
        ),
        migrations.AlterField(
            model_name='rutherfordservice',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
