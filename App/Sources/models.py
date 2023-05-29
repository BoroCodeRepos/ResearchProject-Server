from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Source(models.Model):
    CHARACTER_CHOICE = [
        ("PUB", "Publication"),
        ("OTH", "Other"),
    ]
    title = models.CharField(max_length=20, null=False, default="")
    file = models.FileField(upload_to='Sources/', blank=True, null=True)
    slug = models.SlugField(null=False, unique=True, default="") 
    url = models.URLField(max_length=200, blank=True, default="", null=True) 
    character = models.CharField(max_length=3, choices=CHARACTER_CHOICE, default="PUB", null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('source', kwargs={'slug': self.slug}) 
    
    def clean(self):
        if not self.file and not self.url:
            raise ValidationError('One of the parameters [file/url] is required')
        if self.file and self.url:
            raise ValidationError('Two parameters are given, one is required - file or url')
        super(Source, self).clean()
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
