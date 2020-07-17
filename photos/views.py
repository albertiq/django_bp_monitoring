from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request):
        photos = Photo.objects.all()
        serializer = ArticleSerializer(photos, many=True)
        return Response({"photos": serializer.data})

    def post(self, request, format=None):

        # Create an article from the above data
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)