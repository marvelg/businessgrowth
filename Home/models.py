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

class Welcome(models.Model):
    title = models.CharField(max_length = 120, default = " ")
    subTitle = models.CharField(max_length = 400, blank = True)
    image = models.ImageField(upload_to = "images/", blank = True, default = " ")
    text = RichTextField()

    def __str__(self):
        return "Welcome"

    class Meta:
        verbose_name_plural = "2. Welcome"


class bestService(models.Model):
    exactCategoryName = models.CharField(max_length = 120, help_text = "Category Name", blank = True, default = " ")
    
    def Category(self):
        exactCategoryName = self.exactCategoryName
        return exactCategoryName.replace(" ", "").upper()

    def __str__(self):
        return self.exactCategoryName

    class Meta:
        verbose_name_plural = "3. bestServices"

class Founder(models.Model):
    name = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = "images/", default = "")
    position = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    email = models.EmailField(blank = True)
    detailImage = models.ImageField(upload_to = "images/", default = "")
    detailText = RichTextField(default = "", help_text = "Sub headers should be heading 3")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "4. Founders"

class Client(models.Model):
    imageTitle = models.CharField(max_length = 40, default = " ")
    image = models.ImageField(upload_to = "images/", help_text = "max height = 80px")

    def __str__(self):
        return self.imageTitle

    class Meta:
        verbose_name_plural = "5. Clients"


class Testimonial(models.Model):
    image = models.ImageField(upload_to = "images/")
    testimonial = models.TextField(help_text = "No Quotes Needed")
    name = models.CharField(max_length = 30, blank = True)
    position = models.CharField(max_length = 120, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "6. Testimonials"

class internationalPartner(models.Model):
    imageTitle = models.CharField(max_length = 40, default = " ")
    image = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.imageTitle

    class Meta:
        verbose_name_plural = "7. internationalPartners"