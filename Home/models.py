from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class Home(models.Model):
    image = models.ImageField(upload_to = "images/", blank = True)
    text = RichTextField()