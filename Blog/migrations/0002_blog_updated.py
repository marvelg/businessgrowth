# Generated by Django 2.0.2 on 2018-12-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
