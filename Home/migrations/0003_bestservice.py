# Generated by Django 2.0.2 on 2018-12-18 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_bestservice_client_founder_internationalpartner_slider_testimonial_welcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='bestService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exactCategoryName', models.CharField(blank=True, default=' ', help_text='Category Name', max_length=120)),
            ],
            options={
                'verbose_name_plural': '3. bestServices',
            },
        ),
    ]
