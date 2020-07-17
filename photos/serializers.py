from rest_framework import serializers
from .models import Photo


# class ArticleSerializer(serializers.Serializer):
#     name = serializers.ImageField()
#     title = serializers.CharField(max_length=120)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image_id', 'name')