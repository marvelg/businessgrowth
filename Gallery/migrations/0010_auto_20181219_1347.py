# Generated by Django 2.0.2 on 2018-12-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0009_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name_plural': '5. Videos'},
        ),
        migrations.AddField(
            model_name='video',
            name='videoFile',
            field=models.FileField(blank=True, help_text='(mp4 only) If videoEmbedLink is empty, this video file will be shown', upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='videoEmbedLink',
            field=models.URLField(blank=True, help_text="Video > Share > Embed > src = 'videoEmbedLink' "),
        ),
    ]
