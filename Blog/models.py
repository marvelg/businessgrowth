from django.db import models

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
    date = models.DateField(blank = True, default = "")
    blogCategory = models.CharField(max_length = 60)
    header = models.CharField(max_length = 120, default = "")
    blogDescription = models.TextField()
    editorImage = models.ImageField(upload_to = "images/")
    editor = models.CharField(max_length = 60)

    def properDate(self):
        return self.date.strftime( '%e %B  %Y' )

    def __str__(self):
        return self.header
    class Meta:
        verbose_name_plural = "2. Blogs"