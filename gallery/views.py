from django.shortcuts import render
from django.views.generic import ListView
from .models import ImageUnit

# Create your views here.
class ImageGalleryView(ListView):
    model = ImageUnit
    context_object_name = 'imageunits'
