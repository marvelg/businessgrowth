# Generated by Django 2.0.2 on 2019-01-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0017_auto_20190104_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='detailImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
