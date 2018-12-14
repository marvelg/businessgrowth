from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Slider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "1. Slider"

class Segment(models.Model):
    title = models.CharField(max_length = 120, help_text = "All sub headers should be header 3")
    content = RichTextUploadingField(help_text = "All sub headers should be header 3")
    created = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "2. Segments"
