# Generated by Django 2.0.2 on 2018-12-19 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0007_auto_20181219_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='videosSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': '4. videosSlider',
            },
        ),
        migrations.AlterModelOptions(
            name='imagesslider',
            options={'verbose_name_plural': '1. imagesSlider'},
        ),
    ]
