from django.shortcuts import render, reverse
# gallery view imports
from django.views.generic import ListView, CreateView
from .models import ImageUnit

# upload modal imports
# from django.views.generic.edit import FormView
from .forms import ImageFieldForm

# Create your views here.
class ImageGalleryView(ListView):
    model = ImageUnit
    context_object_name = 'imageunits'

class ImageUploadView(CreateView):
    model = ImageUnit
    template_name = 'gallery/imageupload.html'
    form_class = ImageFieldForm
    success_url = '/'
