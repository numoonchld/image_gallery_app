from django.urls import path
from .views import ImageGalleryView, ImageUploadView, ImageFilterView, ImageDetailView

urlpatterns = [
    path('', ImageGalleryView.as_view(), name='home'),
    path('upload/', ImageUploadView.as_view(), name='upload'),
    path('filtered/<str:image_category>/', ImageFilterView.as_view(), name='filtered_gallery'),
    # path('image/<int:image_id>/', ImageDetailView.as_view(), name='image_detail'),
    path('image/<pk>/', ImageDetailView.as_view(), name='image_detail'),
    
]