from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class Slider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "1. Slider"

class Blog(models.Model):
    image = models.ImageField(upload_to = "images/")
    date = models.DateField(default = "")
    blogCategory = models.CharField(max_length = 60, blank = True)
    header = models.CharField(max_length = 120, default = "")
    blogDescription = models.TextField(blank = True)
    editorImage = models.ImageField(upload_to = "images/")
    editor = models.CharField(max_length = 60, blank = True)
    blogBody = RichTextField(help_text = "subheaders should be header 3", default = "", blank = True)
    
    def properDate(self):
        return self.date.strftime( '%e %B  %Y' )

    def __str__(self):
        return self.header
    class Meta:
        verbose_name_plural = "2. Blogs"
        ordering = ['-date',]