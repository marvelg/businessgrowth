from django.db import models

# Create your models here.
class Slider(models.Model):
    text = models.CharField(max_length = 120)
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = "1. Slider"

class Contact(models.Model):
    city = models.CharField(max_length = 120,)
    location = models.CharField(max_length = 200)
    email = models.EmailField(blank = True)
    number = models.CharField(max_length = 120,blank = True)

    def __str__(self):
        return 'Contact'

    class Meta:
        verbose_name_plural = "2. Contact"