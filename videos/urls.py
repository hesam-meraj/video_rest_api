from django.urls import path
from .views import (
    VideoListView,
    VideoDetailView,
    CategoryListView,
    CategoryDetailView,
    FileListView,
    FileDetailView,
    )


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name="categories-list"),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),


    path('videos/', VideoListView.as_view(), name="videos-list"),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),

    path('videos/<int:video_id>/files/', FileListView.as_view(), name="files-list"),
    path('videos/<int:video_id>/files/<int:pk>/', FileDetailView.as_view(), name="file-detail"),

    
]
