# Generated by Django 2.0.2 on 2018-12-18 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Footer', '0003_whychooseus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': '3. footerAddress'},
        ),
        migrations.AlterModelOptions(
            name='detail',
            options={'verbose_name_plural': '4. footerDetails'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name_plural': '2. footerLinks'},
        ),
        migrations.AlterModelOptions(
            name='whychooseus',
            options={'verbose_name_plural': '1. whyChooseUs'},
        ),
    ]
