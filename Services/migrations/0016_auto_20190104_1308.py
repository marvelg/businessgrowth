# Generated by Django 2.0.2 on 2019-01-04 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0015_auto_20190104_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': '2. serviceCategory'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='created',
        ),
    ]
