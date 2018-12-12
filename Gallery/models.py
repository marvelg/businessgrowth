from django.db import models

# Create your models here.
class Gallery(models.Model):
    imageTitle = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    created = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imageTitle

    class Meta:
        verbose_name_plural = "1. Gallery"

class Certificate(models.Model):
    imageTitle = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    created = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imageTitle
        
    class Meta:
        verbose_name_plural = "2. Certificates"