from rest_framework import serializers
from .models import Category, Video, File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description', 'avatar']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'title', 'file']


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    # if we comment the following line 
    # we just see the id of categories related to the video
    # but we want to have details too!
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'avatar', 'categories', 'files', 'url']