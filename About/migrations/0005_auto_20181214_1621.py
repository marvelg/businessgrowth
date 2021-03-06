# Generated by Django 2.0.2 on 2018-12-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0004_auto_20181212_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': '1. Slider',
            },
        ),
        migrations.AlterModelOptions(
            name='segment',
            options={'verbose_name_plural': '2. Segments'},
        ),
    ]
