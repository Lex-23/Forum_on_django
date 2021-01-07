from django.shortcuts import render
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, \
                         CommentSerializer, \
                         ReplySerializer
from .models import Post, Comment, Reply
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from likes.mixins import LikedMixin, DislikedMixin


class PostViewSet(LikedMixin, DislikedMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

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


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['comment']
    search = ['comment']
    ordering_fields = ['comment', 'author']
    ordering = ['comment', 'author', 'id']
