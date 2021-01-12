from django.shortcuts import render, get_object_or_404
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

class ImageFilterView(ListView):
    model = ImageUnit
    context_object_name = 'imageunits'
    template_name = 'gallery/filteredgallery.html'

    def get_queryset(self): # overrides get
        return ImageUnit.objects.filter(image_category=self.kwargs.get('image_category')).order_by('-image_uploaded_at')