from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Publication(models.Model):
    title = models.CharField(max_length=20, default="")
    file = models.FileField(upload_to='Publications/', unique=True)
    slug = models.SlugField(null=False, unique=True, default="") 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('publication', kwargs={'slug': self.slug}) 
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
