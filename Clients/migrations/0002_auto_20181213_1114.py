# Generated by Django 2.0.2 on 2018-12-13 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': '2. Clients'},
        ),
        migrations.AlterModelOptions(
            name='clientcategory',
            options={'verbose_name_plural': '1. clientCategories'},
        ),
        migrations.AlterField(
            model_name='client',
            name='clientCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Clients', to='Clients.clientCategory'),
        ),
    ]
