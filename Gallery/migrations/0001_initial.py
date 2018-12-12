# Generated by Django 2.0.2 on 2018-12-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageTitle', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': '1. Gallery',
            },
        ),
    ]