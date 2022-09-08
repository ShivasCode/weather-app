from django.db.models.signals import pre_save 
from django.dispatch import receiver
from django.utils.text import slugify

from .models import City

@receiver(pre_save, sender=City)
def auto_add_slug(sender,instance,*args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.city_name)
        print(slug)
        instance.slug = slug 