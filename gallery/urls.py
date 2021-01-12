from django.urls import path
from .views import ImageGalleryView, ImageUploadView, ImageFilterView, ImageDetailView, ImageDeleteView

urlpatterns = [
    path('', ImageGalleryView.as_view(), name='home'),
    path('upload/', ImageUploadView.as_view(), name='upload'),
    path('filtered/<str:image_category>/', ImageFilterView.as_view(), name='filtered_gallery'),
    # path('image/<int:image_id>/', ImageDetailView.as_view(), name='image_detail'),
    path('image/<pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('image/<pk>/delete', ImageDeleteView.as_view(), name='image_delete'),
    
]