from django.db import models
import os
from django.conf import settings

# Create your models here.
class ImageUnit(models.Model):

    CONCEPT_ART = 'CA'
    PRODUCT_DESIGN = 'PD'

    IMAGE_CATEGORIES_CHOICES = [
        (CONCEPT_ART, 'Concept Art'),
        (PRODUCT_DESIGN, 'Product Design'),
    ]
    
    image_title = models.CharField('Title', max_length=50, unique=True)
    image_category = models.CharField('Category',
        max_length=2,
        choices=IMAGE_CATEGORIES_CHOICES,
        default=CONCEPT_ART,
    )
    image_field = models.ImageField('File Selection',upload_to='gallery_images',max_length=500)
    image_uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image_field.name))
        super(ImageUnit,self).delete(*args,**kwargs)