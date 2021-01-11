from django.urls import path
from .views import ImageGalleryView, ImageUploadView

urlpatterns = [
    path('', ImageGalleryView.as_view(), name='home'),
    path('upload/', ImageUploadView.as_view() ,name='upload'),
]