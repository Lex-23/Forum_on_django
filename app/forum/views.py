from django.shortcuts import render

from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.filters import OrderingFilter, SearchFilter


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['category']

    ordering_fields = ['category', 'author']
    ordering = ['category', 'author', 'id']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['post_title']
    search = ['post_title']
    ordering_fields = ['post', 'author']
    ordering = ['post', 'author', 'id']
