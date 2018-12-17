# Generated by Django 2.0.2 on 2018-12-17 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0012_auto_20181217_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='productImage1',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='productImage2',
            new_name='image2',
        ),
        migrations.AlterField(
            model_name='product',
            name='serviceCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Product', to='Services.Service'),
        ),
    ]
