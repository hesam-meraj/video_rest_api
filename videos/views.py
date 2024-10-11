from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Category, Video, File
from .serializers import CategorySerializer, VideoSerializer, FileSerializer


class VideoListView(APIView):

    def get(self, request):
        videos = Video.objects.all()
        # dont forget to set many=True
        serializer = VideoSerializer(videos, many=True, context={'request': request})
        return Response(serializer.data)
    
class VideoDetailView(APIView):

    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = VideoSerializer(video, context={'request': request})
        return Response(serializer.data)


class CategoryListView(APIView):
    
    def get(self, request):
        categories = Category.objects.all()
        serilaizer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serilaizer.data)
    
class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)
    
class FileListView(APIView):
    
    def get(self, request, video_id):
        files = File.objects.filter(video_id=video_id)
        serilaizer = FileSerializer(files, many=True, context={'request': request})
        return Response(serilaizer.data)
    
class FileDetailView(APIView):

    def get(self, request, pk, video_id):
        try:
            file = File.objects.get(pk=pk, video_id=video_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = FileSerializer(file, context={'request': request})
        return Response(serializer.data)