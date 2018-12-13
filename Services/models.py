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

class Service(models.Model):
    category = models.CharField(max_length = 30)
    description = models.TextField(max_length = 220, help_text = "Image height = Text height")
    image = models.ImageField(upload_to = "images/", help_text = "Image height = Text height")
    
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "2. serviceCategory"

class Product(models.Model):
    title = models.CharField(max_length = 50)
    description = RichTextField()
    image1 = models.ImageField(upload_to = "images/", blank = True, help_text = "Optional")
    image2 = models.ImageField(upload_to = "images/", blank = True, help_text = "Optional")
    serviceCategory = models.ForeignKey("Service", related_name = "Product", on_delete = models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "3. Product"