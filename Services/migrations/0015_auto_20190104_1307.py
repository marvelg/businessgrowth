# Generated by Django 2.0.2 on 2019-01-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0014_auto_20181218_1014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['created'], 'verbose_name_plural': '2. serviceCategory'},
        ),
        migrations.AddField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]