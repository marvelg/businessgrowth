# Generated by Django 2.0.2 on 2018-12-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='bestServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=180)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='text',
            field=models.CharField(max_length=120),
        ),
    ]
