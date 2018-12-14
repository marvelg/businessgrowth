from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class clientSlider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "1. clientSlider"
        
class clientCategory(models.Model):
    category = models.CharField(max_length = 100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "2. clientCategories"
class Client(models.Model):
    client = models.CharField(max_length = 100)
    clientCategory = models.ForeignKey("clientCategory", related_name = "Clients", on_delete=models.CASCADE)

    def __str__(self):
        return self.client

    class Meta:
        verbose_name_plural = "3. Clients"

class testimonialSlider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "4. testimonialSlider"

class Testimonial(models.Model):
    header = models.CharField(max_length = 120)
    text = RichTextField()
    def __str__(self):
        return self.header
    class Meta:
        verbose_name_plural = "5. Testimonials"