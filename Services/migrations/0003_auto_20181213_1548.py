# Generated by Django 2.0.2 on 2018-12-13 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='title',
            new_name='category',
        ),
    ]
