# Generated by Django 3.1.7 on 2021-04-14 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_darknesstolight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagesond2l',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='darknesstolight',
            name='image_title',
        ),
        migrations.RemoveField(
            model_name='darknesstolight',
            name='page_description',
        ),
        migrations.RemoveField(
            model_name='darknesstolight',
            name='page_title',
        ),
        migrations.AlterField(
            model_name='darknesstolight',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.imagesond2l'),
        ),
    ]
