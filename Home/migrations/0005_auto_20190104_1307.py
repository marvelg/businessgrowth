# Generated by Django 2.0.2 on 2019-01-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20190102_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcome',
            name='image',
            field=models.ImageField(default=' ', upload_to='images/'),
        ),
    ]