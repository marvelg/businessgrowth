from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class Welcome(models.Model):
    title = models.CharField(max_length = 120, default = "Title goes here")
    subTitle = models.CharField(max_length = 400, blank = True)
    image = models.ImageField(upload_to = "images/")
    text = RichTextField()

    def __str__(self):
        return "Welcome"

    class Meta:
        verbose_name_plural = "Welcome"
    
    