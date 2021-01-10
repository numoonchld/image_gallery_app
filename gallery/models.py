from django.db import models
from django.utils import timezone

# Create your models here.
class ImageUnit(models.Model):
    image_title = models.CharField(max_length = 50)
    image_category = models.TextField()
    image = models.ImageField(upload_to='gallery_images')
    image_uploaded_at = models.DateTimeField(default = timezone.now)