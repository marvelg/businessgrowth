from django.db import models

# Create your models here.
class Slider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "1. Slider"

class Service(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField(max_length = 220, help_text = "Image height = Text height")
    image = models.ImageField(upload_to = "images/", help_text = "Image height = Text height")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "2. Services"