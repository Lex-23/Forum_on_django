from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'text',
            'published',
            'category',
            'url',
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'post_title',
            'author',
            'text',
            'created',
            'updated',
            'active',
            'url',
        )