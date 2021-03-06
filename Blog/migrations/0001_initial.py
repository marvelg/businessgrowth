# Generated by Django 2.0.2 on 2018-12-17 08:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateField(default='')),
                ('blogCategory', models.CharField(blank=True, max_length=60)),
                ('header', models.CharField(default='', max_length=120)),
                ('blogDescription', models.TextField(blank=True)),
                ('editorImage', models.ImageField(upload_to='images/')),
                ('editor', models.CharField(blank=True, max_length=60)),
                ('blogBody', ckeditor.fields.RichTextField(blank=True, default='', help_text='subheaders should be header 3')),
            ],
            options={
                'verbose_name_plural': '2. Blogs',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': '1. Slider',
            },
        ),
    ]
