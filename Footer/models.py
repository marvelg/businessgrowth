from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.    
class Link(models.Model):
    linkTitle = models.CharField(max_length = 50, help_text = "Facebook,Linkedin, etc")
    linkImage = models.ImageField(upload_to = 'images/', help_text = "Can be taken from https://www.flaticon.com/")
    link = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.linkTitle
        
    class Meta:
        verbose_name_plural = "1. Links"

class Address(models.Model):
    address = RichTextField(blank = True)

    def __str__(self):
        return "Address"

    class Meta:
        verbose_name_plural = "2. Address"

class Detail(models.Model):
    header = models.CharField(max_length = 40, help_text = "Office,Email,Mobie,etc")
    detail = models.CharField(max_length = 150, help_text = "+62 82111997750, info@businessgrowthcorp.com, etc")  

    def __str__(self):
        return self.header
        
    class Meta:
        verbose_name_plural = "3. Details"
