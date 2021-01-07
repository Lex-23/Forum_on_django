from rest_framework import serializers
from .models import Post, Comment, Reply
from likes import services as likes_services


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    is_unfan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'author_name',
            'text',
            'published',
            'category',
            'category_name',
            'is_fan',
            'total_likes',
            'is_unfan',
            'total_dislikes',
            'total_comments',
            'status',
            'url',

        )

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` post (`obj`)."""
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)

    def get_is_unfan(self, obj) -> bool:
        """Проверяет, дизлайкнул ли `request.user` post (`obj`)."""
        user = self.context.get('request').user
        return likes_services.is_unfan(obj, user)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'post_title',
            'author',
            'author_name',
            'text',
            'created',
            'updated',
            'active',
            'total_replies',
            'url',
        )


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = (
            'id',
            'comment',
            'author',
            'author_name',
            'text',
            'created',
            'updated',
            'active',
            'url',
        )
