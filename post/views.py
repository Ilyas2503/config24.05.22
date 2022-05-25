from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView

from .models import Post
from .serializers import PostSerializers


class PostView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
