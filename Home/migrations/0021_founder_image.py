# Generated by Django 2.0.2 on 2018-12-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0020_auto_20181212_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='founder',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
