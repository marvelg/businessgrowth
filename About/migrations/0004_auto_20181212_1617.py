# Generated by Django 2.0.2 on 2018-12-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0003_auto_20181212_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
