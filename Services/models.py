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
    category = models.CharField(max_length = 30, help_text = "amount of categories has to be less than or equal to amount of products")
    description = models.TextField(max_length = 220, help_text = "Image height = Text height")
    image = models.ImageField(upload_to = "images/", help_text = "Image height = Text height")
    sliderImage = models.ImageField(upload_to = "images/", default = "")
    title = models.CharField(max_length = 50, blank = True)
    productDescription = RichTextField( blank = True)
    image1 = models.ImageField(upload_to = "images/", blank = True, help_text = "Optional", default = "")
    image2 = models.ImageField(upload_to = "images/", blank = True, help_text = "Optional", default = "")
    detailImage = models.ImageField(upload_to = "images/", default = "", blank = True)
    detail = RichTextField( blank = True)
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "2. serviceCategory"

class Product(models.Model):
    title = models.CharField(max_length = 50, blank = True)
    description = RichTextField( blank = True)
    image1 = models.ImageField(upload_to = "images/", blank = True, help_text = "Optional", default = "")
    image2 = models.ImageField(upload_to = "images/", blank = True, help_text = "Optional", default = "")
    detailImage = models.ImageField(upload_to = "images/", default = "", blank = True)
    detail = RichTextField( blank = True)
    updated = models.DateTimeField(auto_now=True)
    serviceCategory = models.ForeignKey("Service", related_name = "Product", on_delete = models.PROTECT)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "3. Product"