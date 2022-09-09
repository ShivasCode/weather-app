from django.db.models.signals import pre_save 
from django.dispatch import receiver
from django.utils.text import slugify
import re

from .models import City

@receiver(pre_save, sender=City)
def auto_add_slug(sender,instance,*args,**kwargs):
    if instance and not instance.slug:
        word = re.sub(r"\s+", "", instance.city_name, flags=re.UNICODE)
        slug = slugify(word)
        instance.slug = slug