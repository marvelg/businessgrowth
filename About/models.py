from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Segment(models.Model):
    title = models.CharField(max_length = 120, help_text = "All sub headers should be header 3")
    content = RichTextUploadingField(help_text = "All sub headers should be header 3")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "1. Segments"
