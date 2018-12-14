# Generated by Django 2.0.2 on 2018-12-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0002_auto_20181213_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': '1. clientSlider',
            },
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': '3. Clients'},
        ),
        migrations.AlterModelOptions(
            name='clientcategory',
            options={'verbose_name_plural': '2. clientCategories'},
        ),
    ]
