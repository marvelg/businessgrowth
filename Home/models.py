from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class Slider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.text


class Welcome(models.Model):
    title = models.CharField(max_length = 120, default = "Title goes here")
    subTitle = models.CharField(max_length = 400, blank = True)
    image = models.ImageField(upload_to = "images/")
    text = RichTextField()

    def __str__(self):
        return "Welcome"

    class Meta:
        verbose_name_plural = "Welcome"

class bestService(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 220, help_text = "Image height = Text height")
    image = models.ImageField(upload_to = "images/", help_text = "Image height = Text height")
    
    def __str__(self):
        return self.title