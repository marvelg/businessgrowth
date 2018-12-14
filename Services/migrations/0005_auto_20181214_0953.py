# Generated by Django 2.0.2 on 2018-12-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0004_auto_20181213_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(help_text='amount of categories has to be less than or equal to amount of products', max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(help_text='amount of categories has to be less than or equal to amount of products', max_length=30),
        ),
    ]
