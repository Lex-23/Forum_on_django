from rest_framework import serializers
from .models import Post, Comment
from likes import services as likes_services


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'text',
            'published',
            'category',
            'url',
            'is_fan',
            'total_likes',
        )

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` post (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


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