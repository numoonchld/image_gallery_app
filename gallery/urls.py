from django.urls import path
from .views import ImageGalleryView

urlpatterns = [
    path('', ImageGalleryView.as_view() ,name='home')
]