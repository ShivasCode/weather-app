from django.db import models

# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.city_name