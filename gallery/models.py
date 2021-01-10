from django.db import models

# Create your models here.
class ImageUnit(models.Model):
    image_title = models.CharField(max_length = 50)
    image_description = models.TextField()
    image = models.ImageField(upload_to='gallery_images')