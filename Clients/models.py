from django.db import models

# Create your models here.
class clientCategory(models.Model):
    category = models.CharField(max_length = 100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "1. clientCategories"
class Client(models.Model):
    client = models.CharField(max_length = 100)
    clientCategory = models.ForeignKey("clientCategory", related_name = "Clients", on_delete=models.CASCADE)

    def __str__(self):
        return self.client

    class Meta:
        verbose_name_plural = "2. Clients"

