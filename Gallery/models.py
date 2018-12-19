from django.db import models

# Create your models here.
class imagesSlider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "1. imagesSlider"

class Gallery(models.Model):
    imageTitle = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    created = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imageTitle

    class Meta:
        verbose_name_plural = "2. Gallery"

class Certificate(models.Model):
    imageTitle = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    created = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imageTitle
        
    class Meta:
        verbose_name_plural = "3. Certificates"

class videosSlider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "4. videosSlider"

class Video(models.Model):
    videoHeader = models.CharField(max_length = 100)
    videoEmbedLink = models.URLField(max_length = 200,blank = True,help_text = "Video > Share > Embed > src = 'videoEmbedLink' ")
    videoFile = models.FileField(upload_to = "videos/", blank = True,help_text = "(mp4 only) If videoEmbedLink is empty, this video file will be shown")

    def __str__(self):
        return self.videoHeader
    class Meta:
        verbose_name_plural = "5. Videos"